#crear variable
nombre = "Juan"

#imprimir variable
print(nombre)

#crear variable con numero
edad = 30

#imprimir variable
print(edad)

#crear variable con numero decimal
altura = 1.75
#imprimir variable
print(altura)

#crear variable con booleano
es_estudiante = True
#imprimir variable
print(es_estudiante)

#cambiar tipado de variable
nombre = 123
print(type(nombre))

nombre = "Juan"
print(type(nombre))

#concatenacion de variables
saludo = "Hola, mi nombre es " + nombre
print(saludo)

saludo = "Hola, mi nombre es ", nombre, "y tengo ", edad, "años."
print(saludo)

#input y output
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")

edad = input("¿Cuántos años tienes? ")
print("Tienes " + edad + " años.")

#cambiar tipo con input
edad = int(input("¿Cuántos años tienes? "))
print(edad)
print(type(edad))
print("Tienes " + str(edad) + " años.")

