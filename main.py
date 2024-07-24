import pandas as pd
import os

def load_dataset(path):
    _, file_extension = os.path.splitext(path)
    if file_extension == '.csv':
        return pd.read_csv(path)
    elif file_extension == '.xlsx':
        return pd.read_excel(path)
    else:
        raise ValueError("Formato de archivo no soportado. Usar .csv o .xlsx")

def main():
    dataset_path = input("Ingrese nombre del archivo: ")
    try:
        df = load_dataset(dataset_path)
    except ValueError as e:
        print(e)
        return

    df_limpio_columnas = eliminar_columnas_vacias(df)
    df_limpio = eliminar_filas_vacias(df_limpio_columnas)
    print("Después de eliminar columnas con valores nulos o vacíos:")
    print(df_limpio_columnas)
    print("Columnas que quedaron:")
    print(df_limpio_columnas.columns)
    print("Data después de eliminar filas y columnas con valores nulos o vacíos:")
    print(df_limpio)
    
if __name__ == "__main__":
    main()


