ip = int(input("Ingrese el ultimo octeto de la dirección IP: "))

if ip % 2 == 0:
    print("Trafico enrutado al SERVIDOR A (IP par).")
else:
    print("Trafico enrutado al SERVIDOR B (IP impar).")