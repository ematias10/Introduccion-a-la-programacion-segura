def login_protegido():
    contraseña_correcta = "admin123"
    intentos_maximos = 3
    intentos_realizados = 0
    
    while intentos_realizados < intentos_maximos:
        contraseña_usuario = input("Ingrese la contraseña: ")
        if contraseña_usuario == contraseña_correcta:
            print("Acceso al Sistema concedido")
            return
        else:
            intentos_realizados += 1
            print(f"Contraseña incorrecta. Intento {intentos_realizados} de {intentos_maximos}.")
    
    print("CUENTA BLOQUEADA por seguridad.")

# Ejemplo de llamada a la función
login_protegido()
