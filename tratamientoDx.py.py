def eliminar_columnas_vacias(dataframe):

    # Identificar y mostrar columnas con valores nulos
    cols_con_nulos = dataframe.columns[dataframe.isnull().any()].tolist()
    if cols_con_nulos:
        print(f"Columnas con valores nulos: {cols_con_nulos}")
        print("Valores nulos por columna:")
        print(dataframe[cols_con_nulos].isnull().sum())

    dataframe = dataframe.dropna(axis=1)

    # Identificar y mostrar columnas con valores vacíos
    cols_con_vacios = [col for col in dataframe.columns if dataframe[col].apply(lambda x: isinstance(x, str) and x.strip() == '').sum() > 0]
    if cols_con_vacios:
        print(f"Columnas con valores vacíos: {cols_con_vacios}")
        print("Valores vacíos por columna:")
        for col in cols_con_vacios:
            print(f"{col}: {dataframe[col].apply(lambda x: isinstance(x, str) and x.strip() == '').sum()} valores vacíos")

    dataframe = dataframe.drop(columns=cols_con_vacios)

    return dataframe