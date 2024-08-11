

opciones = [0, 1, 2, 3, 4]


for opcion in opciones:
    opcion = int(input("Ingresa opcion "))
    if opcion == 0:
        print(input("Nombre: "))
    elif opcion == 1:
        print(input("Apellido: "))
    elif opcion == 2:
        print(int(input("DNI: ")))
    elif opcion == 3:
        print(input("Fecha de Nacimiento: "))
    elif opcion == 4:
        print(input("Estado civil: "))
    else:
        print("intente nuevamente")


