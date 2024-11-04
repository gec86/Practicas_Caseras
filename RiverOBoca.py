
equipos_grandes = ["River", "Boca", "Racing", "San Lorenzo", "Independiente"]

def cuadro():
    hincha = input("Escriba equipo: ")
    if hincha in equipos_grandes:
        print(f"Es hincha de: ", hincha)
    else:
        print(f"Es de otro equipo")
        

cuadro()