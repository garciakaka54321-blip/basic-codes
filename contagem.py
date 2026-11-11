#contagem de 1 até a 15
import time
for i in range(1, 16):
    print(i)
    time.sleep(1)
    while i == 15:
        print ('A contagem terminou!')
        break