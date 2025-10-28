# leitura  do  led de indicação de energia
led = Pin(4, Pin.OUT) # pino 4 e uma saída /usar um led pisca para facilitar a visualização

print("seja bem vindo wellington e olá cobaia!")
time.sleep(1)
print("iniciando teste de solo...")

import time
import serial as ser

from machine import Pin # controle dos  pinos
from time import sleep # controle de delay do tempo

# Ajuste a porta conforme o sistema
esp = ser.Serial('COM5', 115200, timeout = 1)
# Espera o ESP32 inicializar
time.sleep(1)

# configurações de pinos


#  leitura do sensor de temperatura
tempe = Pin(6, Pin.IN) # pino 6 e a entrada da informação da temperatura
#leitura do módulo do giroscópio
giro = Pin(7,Pin.IN) # pino 7 e a entrada

# leitor de temperatura
while True:
    valor_tempe = tempe.value() #determina que o sensor será lido como um livro
    if 0 <= valor_tempe <= 30: # comparação encadeada /  especifíca o limite de temperatura
        print("temperatura dentro do intervalo certo!") # mensagem na tela
    else:
        print("temperatura fora do padrão.") # mensagem se estiver temperatura fora do padrão
    
    print("leitura concluída.")
    time.sleep(2)

    resposta = input("deseja continuar?\n sim/não").lower()
    if resposta == 'sim':
        print("reiniciado o processo.")
        continue # volta para o inicio de while
    elif resposta == 'não':
        print("passando para o próximo sensor.")
        break # sai do looping
    else:
        print("resposta inválida, reiniciamento de segurança!!!")
        break
