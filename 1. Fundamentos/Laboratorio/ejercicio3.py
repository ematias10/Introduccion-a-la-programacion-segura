#Generacion de Cadena de logs.

ip = input("Ingrese la dirección IP: ")
codigo_HTTP = int(input("Ingrese el código HTTP: "))
nombre_atacante = input("Ingrese el nombre del atacante: ")
log = "IP: ", ip, "- Código HTTP: ", codigo_HTTP, "- Atacante: ", nombre_atacante
print(log)
