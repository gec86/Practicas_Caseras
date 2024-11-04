class persona:
    def __init__(self,p,e):
        self.nombre = p
        self.edad = e
        

p = persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))
print(p.nombre, "cumple", p.edad, "años")