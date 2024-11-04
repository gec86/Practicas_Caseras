class alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print(f"Mi nombre es: ", nombre)
        print(f"Mis apellido es: ", apellido)
    
    def promedio():
        notas = []
        while len(notas) < 3:
            nota = int(input("Esriba la nota: "))
            notas.append(nota)
    
        suma = sum(notas)
        media = suma / len(notas)
        print(notas)
        print(media)
        
        if media >= 4.0:
            print("Aprobaste, pero vas a integrador")
        elif media >= 7.0:
            print("Promocionaste")
        elif media < 3.9:
             print("Recursas")



alumno("Gonzalo", "Corrales")
alumno.promedio()