sueldo_bruto = int(input("Ingrese sueldo bruto: "))

import datetime

actualidad = datetime.datetime.now().year
fecha_ingreso = datetime.datetime(2018, 2, 4).year
antiguedad = actualidad - fecha_ingreso

print("La antiguedad del trabajador es de: ", antiguedad, " años")

porcentaje = (sueldo_bruto*antiguedad)/100
sueldo_antiguedad = sueldo_bruto + porcentaje

aportes = (sueldo_antiguedad*11)/100
print("Aportes jubilatorios: ", aportes)

obra_social = (sueldo_antiguedad*3)/100
print("Descuento de obra social: ", obra_social)

sueldo_neto = sueldo_antiguedad - aportes - obra_social
print("El sueldo neto es de $: ", sueldo_neto)

aguinaldo = sueldo_bruto/2

print("El aguinaldo es de: ", aguinaldo)