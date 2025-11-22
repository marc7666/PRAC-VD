import pandas as pd

df = pd.read_csv(
    "Qualitat_de_l_aire_als_punts_de_mesurament_autom_tics_de_la_Xarxa_de_Vigil_ncia_i_Previsi__de_la_Contaminaci__Atmosf_rica.csv")

df["DATA"] = pd.to_datetime(df["DATA"], dayfirst=True)

# ------------------------------ Filtratge de dades -> A partir de 2015 ------------------------------

df_from_2015_onwards = df[df["DATA"] >= pd.Timestamp("2015-01-01 00:00:00")].copy()  # Bibliografia: [Ref.Codi.5]

# ------------------------------ Tractament de nulls ------------------------------

# -- Si hi ha nulls en les columnes de les lectures -> Imputar un 0 -> Si s'esborra tot el registre per un null a les lectures es perd molta info. --
hours = []
for i in range(1, 25):
    if i < 10:
        hours.append(f"0{i}h")
    else:
        hours.append(f"{i}h")
df_from_2015_onwards[hours] = df_from_2015_onwards[hours].fillna(0)  # Bibliografia: [Ref.Codi.6]

# -- Si hi ha null en alguna d'aquestes columnes (Son les més importants i les que ajudaran a resoldre preguntes) -> Esborrar registre. --
cols = ["DATA", "CONTAMINANT", "UNITATS", "TIPUS ESTACIO", "AREA URBANA", "ALTITUD", "LONGITUD", "LATITUD"]
if df_from_2015_onwards[cols].isnull().any().any():
    df_from_2015_onwards.dropna(subset=cols, inplace=True)  # Bibliografia: [Ref.Codi.7]

# -- Si totes les lectures són 0 -> Esborrar el registre --
df_from_2015_onwards = df_from_2015_onwards[
    ~((df_from_2015_onwards[hours] == 0).all(  # Bibliografia: [Ref.Codi.8] i [Ref.Codi.9]
        axis=1))].copy()

# ------------------------------ Unificació d'unitats en les mesures ------------------------------
# -- ug/m3 = µg/m3
mu_unicode = "\u03bc"  # Bibliografia [Ref.Codi.10]
df_from_2015_onwards["UNITATS"] = df_from_2015_onwards["UNITATS"].replace("ug/m3",
                                                                          f"{mu_unicode}g/m3").copy()  # Bibliografia [Ref.Codi.11]
convert_mili_to_micro = (1.0e-3 / 1.0) * (1.0 / 1.0e-6)  # Convertir a unitat base i d'unitat base a micro
cxonvert_nano_to_micro = (1.0e-9 / 1.0) * (1.0 / 1.0e-6)  # Convertir a unitat base i d'unitat base a micro
