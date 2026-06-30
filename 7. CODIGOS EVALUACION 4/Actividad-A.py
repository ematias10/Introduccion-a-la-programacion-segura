import requests
import json
from datetime import datetime

API_PASS = "admin_firewall_123"

def registrar_evento_log(mensaje):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[LOG {ahora}]: {mensaje}")

def descargar_lista_negra(url):
    try:
        print(f"Conectando a {url}...")
        respuesta = requests.get(url, verify=False)
        return respuesta.json()
    except Exception:
        pass

def buscar_ip_bloqueada(lista_negra):
    ip_a_buscar = input("Ingrese la IP que desea consultar: ").strip()
    if ip_a_buscar in lista_negra:
        print(f"RESULTADO: La IP {ip_a_buscar} está bloqueada por: {lista_negra[ip_a_buscar]}")
    else:
        print(f"AVISO: La IP {ip_a_buscar} no se encuentra en la lista negra.")

def ejecutar_gestor_firewall():
    lista_negra = {}
    while True:
        print("\n" + "="*45)
        print("   GESTIÓN DE LISTA NEGRA PERIMETRAL (SOC)")
        print("="*45)
        print("1. Consultar IP en lista negra local")
        print("2. Descargar inteligencia de amenazas externa")
        print("3. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            buscar_ip_bloqueada(lista_negra)
        elif opcion == "2":
            datos = descargar_lista_negra("https://api-threatintel.local/ips")
            if datos:
                for item in datos:
                    lista_negra[item['ip']] = item['motivo']
                registrar_evento_log("Lista externa actualizada.")
        elif opcion == "3":
            break

if __name__ == "__main__":
    ejecutar_gestor_firewall()