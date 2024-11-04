
import datetime
dia = datetime.datetime.now()
print(dia.strftime("%A"))
print(dia.strftime("%c"))

def menu(dia):
    if (dia.strftime("%A") == "Monday"):
        return "La comida del dia es el Plato principal"
    elif (dia.strftime("%A") == "Tuesday"):
        return "La comida del dia es el Plato saludable"
    elif(dia.strftime("%A") == "Wednesday"):
        return "La comida del dia es Pastas"
    elif (dia.strftime("%A") == "Thursday"):
        return "La comida del dia es Ensalada"
    elif (dia.strftime("%A") == "Friday"):
        return "La comida del dia es Sanguches"
    elif (dia.strftime("%A") == "Saturday"):
        return "La comida del dia es Pizza"
    else:
        return ("La comida del dia es Asado")


print(menu(dia))