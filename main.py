import serial as ser
import time
import binascii as cii
import LoRa
import pandas as pd
import socket

# Ajuste a porta conforme o sistema
esp = ser.Serial('COM5', 115200, timeout=1)
# Espera o ESP32 inicializar
time.sleep(2)

# se ok / Envia comando
esp.write(b"iniciar/n")

# Ler, e responder todo o sistema
resposta = esp.readline().decode().strip()
print("resposta do ESP32", resposta)

#iniciar contagem regressiva

print("iniciar contagem")

# se error(1)
# fazer mais uma leitura do sistema
# localizar o erro
# informar no painel a falha

# se ok 
#iniciar contagem regressiva

# se erro(2) abortar lançamento
