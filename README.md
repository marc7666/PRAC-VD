# Pràctica final dividida en dues parts

Pràctica final de l'assignatura de Visualització de dades del Màster Universitàri en Ciència de Dades de la UOC

## Part I

### Mètriques del dataset original

Llicència del dataset: GENERALITAT DE CATALUNYA. *Llicència d'Ús d'Informació* [en línia]. [Última actualització: 2 de març de 2021] [consulta: 23 de novembre de 2025]. Disponible a: [https://administraciodigital.gencat.cat/ca/dades/dades-obertes/informacio-practica/llicencies/](https://administraciodigital.gencat.cat/ca/dades/dades-obertes/informacio-practica/llicencies/)

- Columnes: Index(['CODI EOI', 'NOM ESTACIO', 'DATA', 'MAGNITUD', 'CONTAMINANT', 'UNITATS', 'TIPUS ESTACIO', 'AREA URBANA', 'CODI INE', 'MUNICIPI', 'CODI COMARCA', 'NOM COMARCA', '01h', '02h', '03h', '04h', '05h', '06h', '07h', '08h', '09h', '10h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h', '22h', '23h', '24h', 'ALTITUD', 'LATITUD', 'LONGITUD', 'Georeferència'], dtype='object')
- Registre més antic: 1991-01-01 00:00:00
- Registre més recent: 2025-11-17 00:00:00
- Contaminants: ['SO2', 'NO2', 'O3', 'NOX', 'PM10', 'NO', 'H2S', 'CO', 'PM2.5', 'Hg', 'Cl2', 'C6H6', 'PM1', 'PS', nan, 'HCT', 'HCNM', 'HCl']
- Tipus d'estació: ['background', 'traffic', 'industrial', nan]
- Tipus d'àrees: ['peri-urban', 'urban', 'rural', 'suburban', nan]
- Unitats de mesura de contaminants: ['µg/m3', 'mg/m3', 'ng/m3', nan, 'ug/m3', 'ppm']
- Total columnes: 40
- Total registres: 3502657

### Mètriques del dataset que s'utilitzarà per a la PRAC

- Columnes: Index(['CODI EOI', 'NOM ESTACIO', 'DATA', 'MAGNITUD', 'CONTAMINANT', 'UNITATS', 'TIPUS ESTACIO', 'AREA URBANA', 'CODI INE', 'MUNICIPI', 'CODI COMARCA', 'NOM COMARCA', '01h', '02h', '03h', '04h', '05h', '06h', '07h', '08h', '09h', '10h', '11h', '12h', '13h', '14h', '15h', '16h', '17h', '18h', '19h', '20h', '21h', '22h', '23h', '24h', 'ALTITUD', 'LATITUD', 'LONGITUD', 'Georeferència'], dtype='object')
- Registre més antic: 2015-01-01 00:00:00
- Registre més recent: 2025-11-17 00:00:00
- Contaminants: ['NO2', 'NOX', 'CO', 'NO', 'PM2.5', 'PM10', 'SO2', 'H2S', 'Hg', 'C6H6', 'O3', 'PM1', 'Cl2']
- Tipus d'estació: ['background', 'traffic', 'industrial']
- Tipus d'àrees: ['urban', 'suburban', 'peri-urban', 'rural']
- Unitats de mesura de contaminants: ['μg/m3']
- Total columnes: 40
- Total registres: 1402163

### Bibliografia

[Ref.1] -- *Calidad del aire en los puntos de medida automáticos de la Red de Vigilancia y Previsión de la Contaminació Atmosférica* [en línia] [consulta: 20 de novembre de 2025] Disponible a: [https://datos.gob.es/es/catalogo/a09002970-calidad-del-aire-en-los-puntos-de-medida-automaticos-de-la-red-de-vigilancia-y-prevision-de-la-contaminacio-atmosferica](https://datos.gob.es/es/catalogo/a09002970-calidad-del-aire-en-los-puntos-de-medida-automaticos-de-la-red-de-vigilancia-y-prevision-de-la-contaminacio-atmosferica)

[Ref.2] -- Generalitat de Catalunya. Departament de Territori, Habitatge i Transició Ecològica. Xarxa de Vigilància i Previsió de la Contaminació Atmosfèrica. [organisme autònom, empresa pública]. *Qualitat de l'aire als punts de mesurament automàtics de la Xarxa de Vigilància i Previsió de la Contaminació Atmosfèrica* [base de dades en línia]. Darrera actualització: [23 de novembre de 2025]. Llicència Oberta d'Ús d'Informació [consulta: 20 de novembre de 2025] Disponible a: [https://analisi.transparenciacatalunya.cat/Medi-Ambient/Qualitat-de-l-aire-als-punts-de-mesurament-autom-t/tasf-thgu/about_data](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Qualitat-de-l-aire-als-punts-de-mesurament-autom-t/tasf-thgu/about_data)

[Ref.3] -- *Sofcatalà* [en línia] [consulta: 20 de novembre de 2025] Disponible a: [https://www.softcatala.org/corrector/](https://www.softcatala.org/corrector/)

### Bibliografia codi

[Ref.Codi.1] -- *pandas.Series.unique* [en línia] [consulta: 20 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html)
 
[Ref.Codi.2] -- *pandas.Series.to_list* [en línia] [consulta: 20 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html)
 
[Ref.Codi.3] -- *Cómo obtener el recuento de filas de un Pandas DataFrame* [en línia] [consulta: 20 de novembre de 2025] Disponible a: [https://www.delftstack.com/es/howto/python-pandas/how-to-get-the-row-count-of-a-pandas-dataframe/](https://www.delftstack.com/es/howto/python-pandas/how-to-get-the-row-count-of-a-pandas-dataframe/)
 
[Ref.Codi.4] -- *pandas.to_datetime* [en línia] [consulta: 20 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
 
[Ref.Codi.5] -- *pandas.DataFrame.copy* [en línia] [consulta: 22 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html)
 
[Ref.Codi.6] -- *pandas.DataFrame.fillna* [en línia] [consulta: 22 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
 
[Ref.Codi.7] -- *pandas.DataFrame.dropna* [en línia] [consulta: 22 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
 
[Ref.Codi.8] -- *pandas.DataFrame.all* [en línia] [consulta: 22 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html)
 
[Ref.Codi.9] -- *Como poner la virgulilla en el teclado (Windows, Mac, Linux, etc)* [en línia] [consulta: 22 de novembre de 2025] Disponible a: [https://www.computermaniaco.com/como-poner-la-virgulilla-en-el-teclado-windows-mac-linux-etc/](https://www.computermaniaco.com/como-poner-la-virgulilla-en-el-teclado-windows-mac-linux-etc/)
 
[Ref.Codi.10] -- *Write \mu (Greek letter, Symbol) in Python Matplotlib.pyplot* [en línia] [consulta: 22 de novembre de 2025] Disponible a: [https://pythonmatplotlibtips.blogspot.com/2017/11/write-mu-greek-letter-symbol-in-python.html](https://pythonmatplotlibtips.blogspot.com/2017/11/write-mu-greek-letter-symbol-in-python.html)
  
[Ref.Codi.11] -- *Python String replace() Method* [en línia] [consulta: 22 de novembre de 2025] Disponible a: [https://www.w3schools.com/python/ref_string_replace.asp](https://www.w3schools.com/python/ref_string_replace.asp)

[Ref.Codi.12] -- *pandas.DataFrame.loc* [en línia] [consulta: 23 de novembre de 2025] Disponible a: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)

[Ref.Codi.13] -- *pandas.DataFrame.to_csv* [en línia] [consulta: 23 de novembre de 2025] Disponible a: [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)