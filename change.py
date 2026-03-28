def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto= float(input("Ingrese el gasto: "))
    dinero= int (input("Ingrese el dinero: "))
    vuelto_pesos= int(dinero-gasto)
    vuelto_centavos= round(((dinero-gasto)-vuelto_pesos) * 100)

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(vuelto_pesos)
    print("Centavos:")
    print(vuelto_centavos)
change()

