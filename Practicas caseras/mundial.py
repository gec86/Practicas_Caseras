mundiales = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 
             1998,2002, 2006, 2010, 2014, 2018, 2022]


for año in mundiales:
    año = int(input("Ingrese año de Mundial: "))
    futuro = año>2024
    if futuro:
        print("El", año, "no llego")
        break
    elif año in mundiales:
        print(f"En", año, "se hizo un Mundial")
    else:
        print(f"En", año, "no se hizo un Mundial")
        break


