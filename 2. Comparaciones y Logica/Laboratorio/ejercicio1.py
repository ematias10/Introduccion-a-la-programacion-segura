
pin = int(input("Ingrese su nuevo PIN de 4 digitos: "))

if pin >= 1000 and pin <= 9999:
    print("PIN VALIDO: Formato correcto.")
else:
    print("PIN NO VALIDO: Debe ser un número de 4 dígitos.")
