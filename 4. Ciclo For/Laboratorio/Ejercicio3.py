# Lista de longitudes de tokens
longitudes_tokens = [6, 12, 25, 0, -4]
# Procesar cada longitud de token utilizando un ciclo for
for longitud in longitudes_tokens:
    if longitud <= 0:
        print(f"Entrada Inválida: Longitud de token imposible ({longitud})")
    elif longitud < 8:
        print(f"Riesgo: Débil ({longitud})")
    elif 8 <= longitud <= 16:
        print(f"Aceptable ({longitud})")
    else:
        print(f"Robusto ({longitud})")
# Al finalizar, mostrar el mensaje de análisis completado
print("Análisis de tokens completado.")
