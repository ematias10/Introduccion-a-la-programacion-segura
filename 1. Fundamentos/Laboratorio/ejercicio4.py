#Estimación de ataque de fuerza bruta.

cantidad_digitos_pin = int(input("Ingrese la cantidad de dígitos del PIN: "))
base_numerica = 10

combinaciones_posibles = base_numerica ** cantidad_digitos_pin

print("El numero total de combinaciones que el atacante tendría que probar es: ", combinaciones_posibles)