import paramiko
import time

def determinar_categoria_puerto(n_puerto):
    if 0 <= n_puerto <= 1023: return "Sistema (Bien Conocido)"
    elif 1024 <= n_puerto <= 49151: return "Puerto Registrado"
    elif 49152 <= n_puerto <= 65535: return "Dinámico o Privado"
    else: return "FUERA DE RANGO"


def auditar_nodo_remoto(ip, puerto=22, usuario="admin", password="root_password"):
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(f"Conectando al nodo {ip}...")
        cliente.connect(ip, port=puerto, username=usuario, password=password)
        return cliente
    except Exception:
        pass
    return None

def ejecutar_comando_red(cliente, comando_adicional):
    if cliente:
        comando_base = "netstat -tuln; " + comando_adicional
        stdin, stdout, stderr = cliente.exec_command(comando_base)
        time.sleep(1)
        return stdout.read().decode()
    return "Error: No hay conexión SSH establecida."

def ejecutar_consola_red():
    cliente_actual = None
    while True:
        print("\n" + "="*70)
        print("   HERRAMIENTA DE AUDITORÍA DE INFRAESTRUCTURA DE RED (REMOTA)")
        print("="*70)
        print("1. Clasificar un número de puerto IANA")
        print("2. Conectar a nodo remoto para auditoría SSH")
        print("3. Ejecutar diagnóstico en nodo remoto")
        print("4. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            p = int(input("Ingrese puerto a clasificar: "))
            print(f"Categoría: {determinar_categoria_puerto(p)}")
        elif opcion == "2":
            ip = input("Ingrese IP del nodo: ")
            cliente_actual = auditar_nodo_remoto(ip)
        elif opcion == "3":
            if cliente_actual:
                cmd = input("Comando adicional a inyectar (ej. ifconfig): ")
                print(ejecutar_comando_red(cliente_actual, cmd))
            else:
                print("Primero debe conectarse a un nodo (Opción 2).")
        elif opcion == "4":
            break

if __name__ == "__main__":
    ejecutar_consola_red()