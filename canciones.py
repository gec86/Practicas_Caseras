Denise_Romano = []

for i in range(5):
    cancion = input(f"Ingrese cancion {i+1}: ")
    cancion = Denise_Romano.append(cancion)

print(Denise_Romano)

cancionero = open("cancionero.txt", "w")
for cancion in Denise_Romano:
    cancionero.write(f"{cancion}\n")

