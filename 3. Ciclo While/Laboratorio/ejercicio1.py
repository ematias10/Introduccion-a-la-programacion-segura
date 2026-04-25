while True:
    token = int(input("Ingrese el token 2FA: "))
    
    if token != 987654:
        print("Token inválido. Reintente.")
    else:
        print("Identidad validada.")
        break
