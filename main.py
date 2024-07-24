import exploracionDx as ex
import tratamientoDx as tr
import os
import pandas as pd

def load_dataset(path):
    _, file_extension = os.path.splitext(path)
    if file_extension == '.csv':
        return pd.read_csv(path)
    elif file_extension == '.xlsx':
        return pd.read_excel(path)
    else:
        raise ValueError("Formato de archivo no soportado. Usar .csv o .xlsx")

def main():
    file_n = input("Por favor digite el nombre del archivo: ")
    try:
        df = load_dataset(file_n)
    except ValueError as e:
        print(e)
        return
    
    exit = False

    while not exit:
        print("Se tienen las siguientes funcionalidades:")
        print("\n")
        print("1. Hallar correlación de pares de variables")
        print("2. Eliminar columnas vacías")
        print("3. Realizar grafica del tipo pairplot")
        print("4. Eliminar filas vacías")
        print("5. Salir")
        print("\n")
        print("Escriba el número de la funcionalidad deseada: ")
        n = int(input())
        print("\n")

        if n == 1:
            ex.corrVar(df)
        elif n == 2:
            df_limpio_columnas = tr.eliminar_columnas_vacias(df)
            print("Después de eliminar columnas con valores nulos o vacíos:")
            print(df_limpio_columnas)
            print("Columnas que quedaron:")
            print(df_limpio_columnas.columns)
        elif n == 3:
            ex.graficar_pairplot(df)
        elif n == 4:
            df_limpio_filas = tr.eliminar_filas_erroneas(df)
            print("DataFrame después de eliminar filas con valores nulos o vacíos:")
            print(df_limpio_filas)
        elif n == 5:
            exit = True
        else:
            print("Número no valido")

        print("\n")

if __name__ == "__main__":
    main()