def verificar_longitud_pass(password):
    # Verificar si la longitud de la contraseña es al menos 8 caracteres
    if len(password) >= 8:
        return True
    else:
        return False
    
# Ejemplo de llamada
resultado = verificar_longitud_pass("12345")
print(f"¿Password segura?: {resultado}")
print("-----------------------------")

resultado = verificar_longitud_pass("Segura123")
print(f"¿Password segura?: {resultado}")
print("-----------------------------")

# EJEMPLO CON VALORES DEL USUARIO
password_usuario = input("Ingrese su contraseña para verificar su longitud: ")
resultado_usuario = verificar_longitud_pass(password_usuario)
print(f"¿Password segura?: {resultado_usuario}")
