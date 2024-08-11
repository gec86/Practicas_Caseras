operador = input("Ingrese signo de operacion: ")

def operaciones(a, b):
    if operador == "+":
        print(a + b)
    elif operador == "-":
        print(a - b)
    elif operador == "*":
        print(a * b)
    elif operador== "/":
        print (a / b)
    else:
        print("Intente nuevamente")



operaciones(20, 10)
    