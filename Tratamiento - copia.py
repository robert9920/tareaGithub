import pandas as pd

def descripcion_estadistica(dataframe, mensaje):
    print(f"\n{mensaje}")
    print(dataframe.describe())


def eliminar_columnas_vacias(dataframe):

    descripcion_estadistica(dataframe, "Descripción estadística antes de eliminar columnas erróneas")
    # Identificar y mostrar columnas con valores nulos
    cols_con_nulos = dataframe.columns[dataframe.isnull().any()].tolist()
    if cols_con_nulos:
        print(f"Columnas con valores nulos: {cols_con_nulos}")
        print("Valores nulos por columna:")
        print(dataframe[cols_con_nulos].isnull().sum())

    dataframe = dataframe.dropna(axis=1)

    # Identificar y mostrar columnas con valores vacíos
    cols_con_vacios = [col for col in dataframe.columns if dataframe[col].apply(lambda x: isinstance(x, str) and x.strip() == '').sum() > 20]
    if cols_con_vacios:
        print(f"Columnas con valores vacíos: {cols_con_vacios}")
        print("Valores vacíos por columna:")
        for col in cols_con_vacios:
            print(f"{col}: {dataframe[col].apply(lambda x: isinstance(x, str) and x.strip() == '').sum()} valores vacíos")

    dataframe = dataframe.drop(columns=cols_con_vacios)

    descripcion_estadistica(dataframe, "Descripción estadística después de eliminar columnas erróneas")

    return dataframe


def eliminar_filas_vacias(dataframe):
    filas_con_nulos = dataframe[dataframe.isnull().any(axis=1)]
    if not filas_con_nulos.empty:
        print("Filas con valores nulos:")
        print(filas_con_nulos)

    dataframe = dataframe.dropna(axis=0)

    filas_con_vacios = dataframe[dataframe.apply(lambda row: any(isinstance(x, str) and x.strip() == '' for x in row), axis=1)]
    if not filas_con_vacios.empty:
        print("Filas con valores vacíos:")
        print(filas_con_vacios)

    dataframe = dataframe[~dataframe.apply(lambda row: any(isinstance(x, str) and x.strip() == '' for x in row), axis=1)]

    return dataframe



if __name__ == "__main__":
    df = pd.read_excel(r'C:\Users\IPNOTICIAS\Documents\Python\Inmuebles.xlsx')

    df_limpio_columnas = eliminar_columnas_vacias(df)
    df_limpio = eliminar_filas_vacias(df_limpio_columnas)
    print("Después de eliminar columnas con valores nulos o vacíos:")
    print(df_limpio_columnas)
    print("Columnas que quedaron:")
    print(df_limpio_columnas.columns)

    print("Data después de eliminar filas y columnas con valores nulos o vacíos:")
    print(df_limpio)