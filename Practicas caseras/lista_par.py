
numeros = [1,2,3,4,5,6,7,8,9,10]

def numeros_par(x):
    return x %2 ==0

def agregar_pares(funcion, lista):
    pares = []
    #return list(filter(funcion, lista))
    for x in lista:
        if funcion(x): #si el importe x esta en la funcion, entonces se agrega
            pares.append(x)
    return pares

print(numeros)
print(agregar_pares(numeros_par, numeros))