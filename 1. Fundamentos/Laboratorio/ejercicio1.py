#Registro de Activos de Red.

host = input("Ingrese el nombre del host: ")
puertos_abiertos = int(input("Ingrese los puertos abiertos: "))
tiempo_actividad_en_horas = float(input("Ingrese el tiempo de actividad en horas: "))
estado_firewall = input("¿El firewall está activo? (Sí/No): ")

print("============================================")
print("Nombre del Host: ", host)
print(type(host))
print("Puertos Abiertos: ", puertos_abiertos)
print(type(puertos_abiertos))
print("Tiempo de Actividad (horas): ", tiempo_actividad_en_horas)
print(type(tiempo_actividad_en_horas))
print("Estado del Firewall: ", estado_firewall)
print(type(estado_firewall))
print("============================================")