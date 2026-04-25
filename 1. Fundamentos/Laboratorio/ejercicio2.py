#Fragmentacion de payload.

tamano_archivo_malicioso = int(input("Ingrese el tamaño del archivo malicioso en bytes: "))
tamano_maximo_paquetes = int(input("Ingrese el tamaño máximo de los paquetes en bytes: "))

numero_paquetes_completos = tamano_archivo_malicioso // tamano_maximo_paquetes
bytes_sobrantes = tamano_archivo_malicioso % tamano_maximo_paquetes
print("Número de paquetes completos: ", numero_paquetes_completos)
print("Bytes sobrantes para el último paquete: ", bytes_sobrantes, "bytes")
