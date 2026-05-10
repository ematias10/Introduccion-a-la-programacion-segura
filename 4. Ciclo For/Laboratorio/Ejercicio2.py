# Solicitar al usuario que ingrese el puerto inicial y final
puerto_inicial = int(input("Ingrese el puerto inicial: "))
puerto_final = int(input("Ingrese el puerto final: "))

# Recorrer el rango de puertos utilizando for i in range(inicio, fin + 1)
for i in range(puerto_inicial, puerto_final + 1):
    print(f"Analizando vulnerabilidades en puerto: {i}")
# Al finalizar, mostrar el mensaje de escaneo completado
print("Escaneo de red completado.")

