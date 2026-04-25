#pedir dos numeros al usuario y mostrar su suma, resta, multiplicacion y division

#pedir dos numeros al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#realizar operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

#mostrar resultados
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)

#division normal, division entera y modulo

division_normal = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2

print("La división normal es: ", division_normal)
print("La división entera es: ", division_entera)
print("El módulo es: ", modulo)

