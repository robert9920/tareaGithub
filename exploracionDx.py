
def corrVar(df):
    print("Su dataframe presenta las siguientes variables del tipo cuantitativo:")
    columns_num = df.select_dtypes("number").columns.tolist()
    print(columns_num)

    print("Escriba el nombre de la primera variable numérica deseada")
    col1 = input()

    print("\n")
    
    while (col1 not in columns_num):
        print("Nombre de variable no válido, por favor seleccionar una variable disponible: ")
        col1 = input()

    print("Ahora escriba el nombre de la segunda variable para conocer la correlación con la primera: ")
    col2 = input()

    while (col2 not in columns_num):
        print("Nombre de variable no válido, por favor seleccionar la segunda variable numeria deseada:  ")
        col2 = input()


    corr = df[col1].corr(df[col2])

    print(f"La correlacion entre la variable 1 y 2 es: {corr:.4f}")