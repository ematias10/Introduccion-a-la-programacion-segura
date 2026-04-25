print("========================================")
print("SISTEMA DE MITIGACIÓN SOC")
print("========================================")
nivel_alerta = int(input("Ingrese nivel de alerta detectado (1-3): "))
print("----------------------------------------")
if nivel_alerta == 1:
    print("MITIGACIÓN AUTOMÁTICA:")
    print("Nivel Bajo: Registrando evento en bitácora.")
elif nivel_alerta == 2:
    print("MITIGACIÓN AUTOMÁTICA:")
    print("Nivel Medio: Aislando host comprometido.")
elif nivel_alerta == 3:
    print("MITIGACIÓN AUTOMÁTICA:")
    print("Nivel Crítico: Apagando interfaz de red exterior.")
else:
    print("Error: Código de alerta desconocido. Revise el sensor.")
print("========================================")
