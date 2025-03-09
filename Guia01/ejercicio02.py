import datetime

# Pedir la fecha de nacimiento al usuario
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (formato: DD/MM/AAAA): ")

# Convertir la cadena en un objeto datetime
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

# Determinar el mes y el día de la fecha de nacimiento
mes = fecha_nacimiento.month
dia = fecha_nacimiento.day

# Determinar la estación en base al mes y día
if (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "Primavera"
elif (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "Otoño"
else:
    estacion = "Invierno"

print(f"Tu fecha de nacimiento corresponde a la estación de {estacion}.")
