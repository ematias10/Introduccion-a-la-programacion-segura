import subprocess
import hashlib
import os
from datetime import datetime

def obtener_tiempo():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def registrar_evidencia_triage(datos):
    ruta_tmp = "/tmp/triage_evidencia.txt"
    with open(ruta_tmp, "a") as f:
        f.write(datos + "\n")

def aislar_host_comprometido(ip):
    timestamp = obtener_tiempo()
    print(f"\n[CRITICAL - {timestamp}] Iniciando aislamiento lógico...")
    comando = f"iptables -A INPUT -s {ip} -j DROP"
    subprocess.Popen(comando, shell=True)
    print("ESTADO: Host aislado.")

def generar_firma_alerta(alerta_texto):
    hasher = hashlib.md5()
    hasher.update(alerta_texto.encode())
    return hasher.hexdigest()

def iniciar_sistema_triaje():
    while True:
        print("\n" + "="*60)
        print("   SISTEMA DE TRIAJE Y RESPUESTA A INCIDENTES (SRI)")
        print("="*60)
        print("1. Aislar host crítico")
        print("2. Generar firma de alerta")
        print("3. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            ip = input("Ingrese IP a bloquear: ")
            aislar_host_comprometido(ip)
        elif opcion == "2":
            texto = input("Ingrese texto de la alerta: ")
            firma = generar_firma_alerta(texto)
            print(f"Firma MD5 de la alerta: {firma}")
            registrar_evidencia_triage(f"Alerta: {texto} | Hash: {firma}")
        elif opcion == "3":
            break

if __name__ == "__main__":
    iniciar_sistema_triaje()