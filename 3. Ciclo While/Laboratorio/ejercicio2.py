intentos = 0
while intentos < 3:
    clave_intento = input("Ingrese la clave de acceso: ")
    
    if clave_intento == "Chil3_S3gur0":
        print("Acceso concedido al sistema.")
        break
    else:
        intentos += 1
        print("Clave errónea. Intento", intentos, "de 3.")
else:
    print("CUENTA BLOQUEADA.")
