
#VARIABLES DE ENTRADA
#evitar usar ñ y caracteres especiales para los nombres de las variables, ya que pueden generar errores en algunos entornos de programación.
#por ejemplo, en lugar de usar "tamaño_alfabeto", se puede usar "tamano_alfabeto".
tamano_alfabeto = int(input("Ingrese el tamaño de caracteres del alfabeto de la contraseña (10 o 26): "))
longitud_contrasena = int(input("Ingrese la longitud de la contraseña: "))
velocidad_ataque = int(input("Ingrese la velocidad de ataque en intentos por segundo: "))
tamano_kb = float(input("Ingrese el tamaño de cada registro de logs en KB: "))

#VARABLES DE PROCESAMIENTO
total_combinaciones = tamano_alfabeto ** longitud_contrasena
tiempo_total_segundos = total_combinaciones / velocidad_ataque
tamano_total_logs = (total_combinaciones * tamano_kb) / 1024  # Convertir KB a MB

#para convertir el tiempo total a unidades más comprensibles, como minutos, horas o días, se pueden usar las siguientes conversiones:
tiempo_total_horas = tiempo_total_segundos // 3600 # Convertir segundos a horas
resto = tiempo_total_segundos % 3600 # el resto de segundos después de convertir a horas
tiempo_total_minutos = resto // 60 # Convertir el resto a minutos
tiempo_total_segundos_final = resto % 60 # el resto de segundos después de convertir a minutos


print("============================================")
print("SIMULADOR DE ATAQUE DE FUERZA BRUTA")
print("============================================")

print("Total de combinaciones a probar:" , total_combinaciones)
print("Velocidad de ataque: " , velocidad_ataque, " intentos por segundo")
print("--------------------------------")

print("TIEMPO ESTIMADO DE COMPROMISO:")
print("El ataque tardaria ", tiempo_total_segundos, " segundos en total")
print("Lo que equivale a ", tiempo_total_horas, " horas, ", tiempo_total_minutos, " minutos y ", tiempo_total_segundos_final, " segundos.")
print("--------------------------------")

print("IMPACTO EN INFRAESTRUCTURA DE LOGS:")
print("Los intentos fallidos generarían ", tamano_total_logs, " MB de logs")

print("============================================")

