america = ["Argentina", "Brasil", "Uruguay", "Colombia", "Ecuador", "Bolivia",
           "Venezuela", "Mexico", "Estados Unidos", "Canada", "Paraguay"]
europa = ["Italia", "Francia", "España", "Alemania", "Inglaterra", "Portugal", 
          "Polonia", "Rumania", "Irlanda", "Paises Bajos"]
asia = ["Japon", "China", "Corea", "Vietnam", "Indonesia"]
africa = ["Nigeria", "Camerun", "Senegal", "Mozambique", "Sudafrica", "Marruecos",
          "Ghana", "Cabo Verde", "Egipto", "Argelia"]
oceania = ["Australia", "Nueva Zelanda"]


while True:
    pais = input("Elija pais: ")
    
    if pais in america:
        print("Pais americano:")
    elif pais in europa:
        print("Pais europeo")
    elif pais in africa:
        print("Pais africano")
    elif pais in asia:
        print("Pais asiatico")
    elif pais in oceania:
        print("Pais oceanico")
    else:
        print("No esta en la lista. Gracias")
        break


