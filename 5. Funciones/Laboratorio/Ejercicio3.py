def filtrar_trafico(puerto):
    # Lista de puertos permitidos
    puertos_permitidos = [22, 80, 443]
    
    # Verificar si el puerto está en la lista de permitidos
    if puerto in puertos_permitidos:
        print(f"Tráfico PERMITIDO en puerto {puerto}")
    else:
        print(f"Tráfico BLOQUEADO en puerto {puerto}")

# Ejemplo de llamadas a la función
filtrar_trafico(443)  # Tráfico PERMITIDO en puerto 443
print("-----------------------------")
filtrar_trafico(3306) # Tráfico BLOQUEADO en puerto 3306
print("-----------------------------")

# EJEMPLO CON VALORES DEL USUARIO
puerto_usuario = int(input("Ingrese el número de puerto a filtrar: "))
filtrar_trafico(puerto_usuario)
