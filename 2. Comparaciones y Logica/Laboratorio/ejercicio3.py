puerto = int(input("Ingrese el número del puerto: "))

if puerto >= 0 and puerto <= 1023:
    print("El puerto es un puerto bien conocido.")

elif puerto >= 1024 and puerto <= 49151:
    print("El puerto es un puerto registrado.")

elif puerto >= 49152 and puerto <= 65535:
    print("El puerto es un puerto dinámico o privado.")

else:
    print("El número de puerto ingresado no es válido.")
    