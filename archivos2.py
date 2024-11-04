from pathlib import Path
DIRECTORIO_BASE = Path(__file__).resolve().parent
ARCHIVO = "prueba.txt"
RUTA = DIRECTORIO_BASE / ARCHIVO
print(RUTA)
archivo = open(RUTA, "w")
archivo.write("abc\n")
archivo.write("cde")
archivo.close()
archivo = open(RUTA, "a")
archivo.write("\nfgh")
archivo.write("\nijk")
archivo.close()
archivo = open(RUTA, "r")
lectura = archivo.read()
print(lectura)