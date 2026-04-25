while True:
    print("=================================================")
    print("CONSOLA DE GESTIÓN SOC - NIVEL MCTP 3")
    print("================================================")
    print("--- MENÚ DE HERRAMIENTAS DE RESPUESTA ---")
    print("1. Monitoreo de Tráfico")
    print("2. Bloqueo de IP Maliciosa")
    print("3. Verificación de Integridad (Hashes)")
    print("4. Salir del Sistema")
    print("-------------------------------------------------")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("EJECUTANDO: Monitoreo de Tráfico")
        # Aquí se implementaría la lógica de monitoreo de tráfico
        print("Monitoreo de tráfico en curso...")

    elif opcion == 2:
        print("EJECUTANDO: Control de Acceso Perimetral")
        ip_origen = input("Ingrese IP de origen para análisis: ")
        # Aquí se implementaría la lógica de bloqueo de IP maliciosa
        print("ACCESO DENEGADO: IP identificada en lista negra.")
        print("Acción de bloqueo registrada en la bitácora SIEM.")
    
    elif opcion == 3:
        print("EJECUTANDO: Auditoría de Integridad de Archivos")
        hash_original = input("Ingrese Hash SHA-256 original: ")
        hash_recibido = input("Ingrese Hash del archivo recibido: ")
        # Aquí se implementaría la lógica de verificación de integridad
        if hash_original == hash_recibido:
            print("Integridad confirmada: El archivo no ha sido alterado.")
        else:
            print("Integridad comprometida: El archivo ha sido alterado.")
    
    elif opcion == 4:
        print("Cerrando consola de seguridad...")
        print("Sesión finalizada correctamente.")
        break

    else:
        print("ERROR: Opción fuera de rango. Por favor, reintente.")
    print("-------------------------------------------------")
