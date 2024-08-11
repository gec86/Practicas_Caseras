edad = (input("Dime tu edad: "))
if edad.isdigit():
    edad = int(edad)
    print(f"Naciste en el año {2024-edad}")