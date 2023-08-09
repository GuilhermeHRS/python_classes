from datetime import datetime, timedelta
import time

inicio_contador = datetime.now()

contador = 0
user_cont = float(input("Write here: "))
while contador < user_cont:
    print("Contagem:", contador)
    contador += 1
    time.sleep(0.01)

fim_contador = datetime.now()

tempo_total_decorrido = fim_contador - inicio_contador
print("Tempo Total Decorrido:", tempo_total_decorrido)
