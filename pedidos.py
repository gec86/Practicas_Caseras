
def cliente(nombre):
    print(nombre)


comida = ["Plato del dia", "Pastas", "Saludable", "Sanguche", "Hamburguesa", "Pizza"]
bebidas = ["Agua", "Coca cola", "Agua saborizada", "Licuado", "Cerveza", "vino"]
postres = ["Helado", "Torta", "Flan", "Merengue", "Fruta", "Ensalada de fruta"]
medio_pago =["Efectivo", "Debito", "Credito", "Mercado Pago"]




cliente("Gonzalo")
print("comera", comida[2])
print("tomará", bebidas[5])
print("y de postre: ", postres[2])
costo = int(input("Costo total: "))
print("el importe de", costo, " lo pagara con: ", medio_pago[3])


