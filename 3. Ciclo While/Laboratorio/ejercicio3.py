espacio_gb = 5.0

while espacio_gb > 2.0:
    print(f"Registrando evento... Espacio restante: {espacio_gb} GB")
    espacio_gb -= 0.5

print("ALERTA: Espacio crítico. Rotación de logs necesaria.")
