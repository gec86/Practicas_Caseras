balance = [
    ["Enero", 23000, 30000],
    ["Febrero", 31000, 15000],
    ["Marzo", 30000, 30000],
    ["Abril", 14000, 7000],
    ["Mayo", 35000, 31000],
    ["Junio", 10000, 30000],
    ["Julio", 20000, 5000],
    ["Agosto", 100000, 65000],
    ["Septiembre", 45000, 30000],
    ["Octubre", 70000, 80000],
    ["Noviembre", 86000, 85000],
    ["Diciembre", 1000, 4000],
]


mes= balance[int(input("Ingrese mes: "))][0]
ingreso = balance[int(input("Ingrese ingreso: "))][1]
egreso = balance[int(input("Ingrese egreso: "))][2]

string = mes
int = ingreso
int = egreso

print(f"El ingreso del mes de {mes} es de $", ingreso)
print(f"El egreso es del mes de {mes} es de $ ", egreso)



def saldo():
    if (ingreso > egreso):
        print("Hay ganancia")
    elif (ingreso == egreso):
        print("No paso nada")
    elif (ingreso < egreso):
        print("Hay perdida")


saldo()