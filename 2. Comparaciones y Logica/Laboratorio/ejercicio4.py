# Solicitar datos al usuario
monto = int(input("Ingrese el monto de la transferencia: "))
pais_destino = input("Ingrese el país de destino: ")
transferencias_hoy = int(input("Ingrese la cantidad de transferencias realizadas hoy: "))

# Evaluar si la transferencia es sospechosa
if (monto > 500000 and pais_destino != "Chile") or transferencias_hoy > 10:
    print("ALERTA ANTI-FRAUDE: Transacción bloqueada por actividad sospechosa")
else:
    print("TRANSACCIÓN APROBADA: Comportamiento normal")
