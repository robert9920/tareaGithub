import exploracionDx as ex
import os
import pandas as pd

def main():

    file_n = input("Por favor digite el nombre del archivo: ")

    extension = os.path.splitext(file_n)[1]

    if extension == ".csv":
        df = pd.read_csv(file_n)
    elif extension == ".xlsx":
        df = pd.read_excel(file_n)
    else:
        raise ValueError("Formato no soportado o archivo no encontrado. Solo se acepta .csv o .xlsx")
    
    exit = False

    while not (exit):
        print("Se tienen las siguientes funcionalidades:")
        print("\n")
        print("1. Hallar correlación de pares de variables")
        print("2. Salir")
        print("\n")
        print("Escriba el número de la funcionalidad deseada: ")
        n = int(input())
        print("\n")

        if (n == 1):
            ex.corrVar(df)
        elif (n == 2):
            exit = True
        else:
            print("Número no valido")

        print ("\n")


if __name__ == "__main__":
    main()