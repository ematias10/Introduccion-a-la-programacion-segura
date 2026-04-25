print("========================================")
print("SISTEMA DE ACCESO VPN SEGURO")
print("========================================")

nobmre_usuario = input("Ingrese su nombre de usuario: ")

if nobmre_usuario == "admin":
    token = int(input("Ingrese su token numérico: "))
    if token == 1234:
        print("----------------------------------------")
        print("Acceso concedido a la VPN. Conectando...")
        print("========================================")
    else:
        print("----------------------------------------")
        print("Error: Token inválido, sesión bloqueada.")
        print("========================================")
else:
    print("----------------------------------------")
    print("Acceso denegado: Usuario no registrado.")
    print("========================================")
