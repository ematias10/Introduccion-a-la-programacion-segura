# Solicitar al usuario que ingrese una contraseña
password = input("Ingrese su contraseña: ")
# Inicializar banderas para verificar los requisitos
es_mayuscula = False
tiene_numero = False

# Recorrer cada carácter de la contraseña
for i in password:
    # Verificar si el carácter es una letra mayúscula
    if i.isupper():
        es_mayuscula = True
    # Verificar si el carácter es un número
    if i.isdigit():
        tiene_numero = True

# Verificar si ambos requisitos se cumplen
if es_mayuscula and tiene_numero:
    print("ÉXITO: La contraseña cumple con los estándares")
else:
    print("FALLA: La clave debe tener al menos una Mayúscula y un Número")
