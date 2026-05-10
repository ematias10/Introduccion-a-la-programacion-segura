def escaner_puertos(puerto_inicio, puerto_fin):
    # Validar que el rango de puertos sea coherente
    if puerto_inicio < 0 or puerto_fin < 0:
        print("Error: Los puertos no pueden ser negativos.")
        return
    if puerto_inicio > puerto_fin:
        print("Error: El puerto inicial debe ser menor o igual al puerto final.")
        return
    
    # Iterar desde puerto_inicio hasta puerto_fin
    for puerto in range(puerto_inicio, puerto_fin + 1):
        print(f"Puerto {puerto} escaneado correctamente.")
    
    # Mensaje de término
    print("Análisis de puertos completado.")

# Ejemplo de llamada a la función
escaner_puertos(10, 20)
print("-----------------------------")

escaner_puertos(20, 10)  # Ejemplo de error por rango incoherente
print("-----------------------------")

escaner_puertos(-5, 10)  # Ejemplo de error por puerto negativo
print("-----------------------------")

# EJEMPLO CON VALORES DEL USUARIO
puerto_inicio = int(input("Ingrese el puerto de inicio: "))
puerto_fin = int(input("Ingrese el puerto de fin: "))
escaner_puertos(puerto_inicio, puerto_fin)