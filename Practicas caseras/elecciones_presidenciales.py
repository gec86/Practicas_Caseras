
Milei = int(input("Cantidad de votos de Milei: "))
Massa = int(input("Cantidad de votos de Massa: "))
Schiaretti = int(input("Cantidad de votos de Schiaretti: "))
Bullrich = int(input("Cantidad de votos de Bullrich: "))
Bregman = int(input("Cantidad de votos de Bregman: "))

votos_totales = Milei + Massa + Schiaretti + Bullrich + Bregman

print(votos_totales)

def resultados():
    porcentaje_1 = round((Milei * 100) / votos_totales, 2)
    porcentaje_2 = round((Massa * 100) / votos_totales, 2)
    porcentaje_3 = round((Schiaretti * 100) / votos_totales, 2)
    porcentaje_4 = round((Bullrich * 100) / votos_totales, 2)
    porcentaje_5 = round((Bregman * 100) / votos_totales, 2)
    print("Javier Milei obtubvo el", porcentaje_1, "% por ciento de los votos")
    print("Sergio Massa obtubvo el", porcentaje_2, "% por ciento de los votos")
    print("Schiaretti obtubvo el", porcentaje_3, "% por ciento de los votos")
    print("Patricia Bullrich obtubvo el", porcentaje_4, "% por ciento de los votos")
    print("Miryam Bregman obtubvo el", porcentaje_5, "% por ciento de los votos")


resultados()