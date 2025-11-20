import pandas as pd


def get_dataframe_info(data: pd.DataFrame) -> list:
    result = []
    headers = data.columns
    result.append(headers)
    min_date = min(data["DATA"])
    result.append(min_date)
    max_date = max(data["DATA"])
    result.append(max_date)
    pollutants = data["CONTAMINANT"].unique().tolist() # Bibliografia: [Ref.Codi.1] i [Ref.Codi.2]
    result.append(pollutants)
    station_types = data["TIPUS ESTACIO"].unique().tolist()
    result.append(station_types)
    area_types = data["AREA URBANA"].unique().tolist()
    result.append(area_types)
    measurement_units = data["UNITATS"].unique().tolist()
    result.append(measurement_units)
    total_cols = data.shape[1] # Bibliografia: [Ref.Codi.3]
    result.append(total_cols)
    total_rows = data.shape[0]
    result.append(total_rows)
    return result


if __name__ == "__main__":
    df = pd.read_csv(
        "Qualitat_de_l_aire_als_punts_de_mesurament_autom_tics_de_la_Xarxa_de_Vigil_ncia_i_Previsi__de_la_Contaminaci__Atmosf_rica.csv")
    print("------------------------------ Dades abans del filtratge ------------------------------")
    df["DATA"] = pd.to_datetime(df["DATA"], dayfirst=True) # Bibliografia: [Ref.Codi.4]
    data_before_filter = get_dataframe_info(df)
    print(f"Columnes: {data_before_filter[0]}")
    print(f"Registre més antic: {data_before_filter[1]}")
    print(f"Registre més recent: {data_before_filter[2]}")
    print(f"Contaminants: {data_before_filter[3]}")
    print(f"Tipus d'estació: {data_before_filter[4]}")
    print(f"Tipus d'àrees: {data_before_filter[5]}")
    print(f"Unitats de mesura de contaminants: {data_before_filter[6]}")
    print(f"Total columnes: {data_before_filter[7]}")
    print(f"Total registres: {data_before_filter[8]}")
    print("------------------------------ Dades després del filtratge ------------------------------")
    df_from_2015_onwards = df[df["DATA"] >= pd.Timestamp("2015-01-01")]
    data_after_filter = get_dataframe_info(df_from_2015_onwards)
    print(f"Registre més antic: {data_after_filter[1]}")
    print(f"Registre més recent: {data_after_filter[2]}")
    print(f"Contaminants: {data_after_filter[3]}")
    print(f"Tipus d'estació: {data_after_filter[4]}")
    print(f"Tipus d'àrees: {data_after_filter[5]}")
    print(f"Unitats de mesura de contaminants: {data_after_filter[6]}")
    print(f"Total registres: {data_after_filter[8]}")