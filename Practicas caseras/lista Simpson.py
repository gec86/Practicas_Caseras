Simpsons = ["Bart", "Lisa", "Homero", "Maggie", "Marge", "Moe", "Barney", "Otto"]

oportunidades = 3
acertados = 0

while oportunidades > 0:
    personaje = input("Agregue personaje: ")
    if personaje in Simpsons:
        acertados = acertados + 1
        print(f"Acertaste ", acertados)
        continue
    else:
        oportunidades = oportunidades - 1
        print(f"Te equivocaste y te quedan ", oportunidades)


        