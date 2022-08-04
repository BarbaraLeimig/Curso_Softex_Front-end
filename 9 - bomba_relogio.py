#bomba_relogio

import time
start_time = 20
end_time = 0

print("Atenção: Você tem 20s para deixar o recinto antes da explosão!")
print("Iniciando contagem regressiva:")
for t in range(start_time, end_time, -1):
    print(t)
    time.sleep(1)
print("BUM!!!")