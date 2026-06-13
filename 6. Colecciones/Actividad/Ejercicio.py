#Crear listas y diccionarios iniciales
lista_logs = []
puertos_bloqueados = [22, 23, 80, 443]

registro_ips = {
    '192.168.1.1': 'Se realizo un ataque DoS',
}

#Funciones para cada opción del menú

#Función para simular un ataque DoS
def simular_dos(ip, registro_ips, lista_logs):
    registro_ips[ip] = 'Realizo un ataque DoS'
    lista_logs.append(f"Se realizó un ataque DoS en el sistema")
    print(f"Simulación de ataque DoS desde la IP {ip} realizada.")

#Función para simular un ataque de fuerza bruta
def simular_fuerza_bruta(ip, registro_ips, lista_logs):
    registro_ips[ip] = 'Realizo un ataque de fuerza bruta'
    lista_logs.append(f"Se realizó un ataque de fuerza bruta en el sistema")
    print(f"Simulación de ataque de fuerza bruta desde la IP {ip} realizada.")

#Función para acceder a un puerto
def acceder_puerto(ip, puerto, registro_ips, lista_logs):
    if puerto in puertos_bloqueados:
        print(f"Acceso denegado al puerto {puerto}. El puerto está bloqueado.")
        registro_ips[ip] = f"Intentó acceder al puerto {puerto} bloqueado"
        lista_logs.append(f"Intento de acceso al puerto {puerto} bloqueado desde la IP {ip}")
    else:
        print(f"Acceso permitido al puerto {puerto}.")
        lista_logs.append(f"Acceso al puerto {puerto} desde la IP {ip}")

#Función para bloquear un puerto
def bloquear_puerto(puerto):
    if puerto not in puertos_bloqueados:
        puertos_bloqueados.append(puerto)
        print(f"Puerto {puerto} bloqueado exitosamente.")
    else:
        print(f"El puerto {puerto} ya está bloqueado.")

#Función para ver registros de IPs
def ver_registros_ips(registro_ips):
    print("Registros de IPs:")
    for ip, actividad in registro_ips.items():
        print(f"{ip}: {actividad}")

#Función para ver registro de logs
def ver_registro_logs(lista_logs):
    print("Registro de Logs:")
    for contador, log in enumerate(lista_logs, start=1):
        print(f"{contador}] {log}")

#Función para ver puertos bloqueados
def ver_puertos_bloqueados(puertos_bloqueados):
    print("Puertos bloqueados:")
    for puerto in puertos_bloqueados:
        print(f"- Puerto {puerto}")


#MENU PERSISTENTE de opciones
while True:
    print("==========================================")
    print("                 SISTEMA SOC")
    print("==========================================")
    print("1] Simular ataque DoS")
    print("2] Simular ataque de fuerza bruta")
    print("3] Acceder a puerto")
    print("4] Bloquear un puerto")
    print("5] Ver registros de IPs")
    print("6] Ver registro de logs")
    print("7] Ver puertos bloqueados")
    print("8] Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    if opcion == 1:
        ip_usuario = input("Ingrese la IP del atacante: ")
        simular_dos(ip_usuario, registro_ips, lista_logs)

    elif opcion == 2:
        ip_usuario = input("Ingrese la IP del atacante: ")
        simular_fuerza_bruta(ip_usuario, registro_ips, lista_logs)

    elif opcion == 3:
        ip_usuario = input("Ingrese la IP del usuario: ")
        try:
            puerto = int(input("Ingrese el puerto al que desea acceder: "))
            acceder_puerto(ip_usuario, puerto, registro_ips, lista_logs)
        except ValueError:
            print("Por favor, ingrese un número de puerto válido.")
            continue

    elif opcion == 4:
        try:
            puerto = int(input("Ingrese el puerto que desea bloquear: "))
            bloquear_puerto(puerto)
        except ValueError:
            print("Por favor, ingrese un número de puerto válido.")
            continue

    elif opcion == 5:
        ver_registros_ips(registro_ips)

    elif opcion == 6:
        ver_registro_logs(lista_logs)

    elif opcion == 7:
        ver_puertos_bloqueados(puertos_bloqueados)

    elif opcion == 8:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
    print("\n")
