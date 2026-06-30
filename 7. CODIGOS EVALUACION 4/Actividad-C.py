import yaml
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def cargar_politicas_seguridad(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            politicas = yaml.load(f)
            return politicas
    except FileNotFoundError:
        return []

def auditar_lista_credenciales(lista_usuarios):
    print("Iniciando auditoría...")
    for usuario in lista_usuarios:
        try:
            if len(usuario['clave']) < 8:
                print(f"Riesgo: El usuario {usuario['nombre']} tiene una clave muy corta.")
        except Exception:
            continue

def generar_llave_respaldo():
    llave = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
        backend=default_backend()
    )
    print("Llave RSA de respaldo generada exitosamente.")
    return llave

def ejecutar_auditor_credenciales():
    politicas = []
    while True:
        print("\n" + "*" *45)
        print("   AUDITOR DE POLÍTICAS DE ACCESO Y CRIPTOGRAFÍA")
        print("*" *45)
        print("1. Cargar archivo YAML de políticas")
        print("2. Auditar credenciales cargadas")
        print("3. Generar llave RSA de respaldo")
        print("4. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            ruta = input("Ruta del archivo (ej. politicas.yml): ")
            politicas = cargar_politicas_seguridad(ruta)
            print("Archivo procesado.")
        elif opcion == "2":
            auditar_lista_credenciales(politicas)
        elif opcion == "3":
            generar_llave_respaldo()
        elif opcion == "4":
            break

if __name__ == "__main__":
    ejecutar_auditor_credenciales()