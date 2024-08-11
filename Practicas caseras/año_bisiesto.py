

año = int(input("Ingrese año: "))

def bisiesto(año):
    if(año % 4 == 0):
        print(f"El año {año} es bisiesto")
    else:
        print(f"EL año {año} no es bisiesto")
    


bisiesto(año)



