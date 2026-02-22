gastos = []
print("#--------------------------#")
print("#--| registro de gastos |--#")
print("#--------------------------#")
while True:
    print("\nopciones:")
    print("1. agregar un gasto")
    print("2. mostrar gastos")
    print("3. mostrar total de gastos")
    print("0. salir")
    opcion = input("seleccione una opcion: ")
    if opcion == "1":
        try:
            monto = float(input("ingrese el valor del gasto: "))
            gastos.append(monto)
            print(f"gasto de {monto} registrado correctamente.")
        except ValueError:
            print("entrada invalida, por favor ingrese un numero valido.")
    elif opcion == "2":
        if len(gastos) > 0:
            print("lista de gastos:")
            for i, gasto in enumerate(gastos, start=1):
                print(f"{i}. {gasto}")
        else:
            print("no hay gastos registrados.")
    elif opcion == "3":
        total = sum(gastos)
        print(f"total de gastos: {total}")
    elif opcion == "0":
        print("saliendo del registro de gastos...")
        break
    else:
        print("opcion invalida, intente nuevamente.")