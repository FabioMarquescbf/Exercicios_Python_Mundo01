import random
from time import sleep
computador = (0, 1, 2, 3, 4, 5)
zorteio = random.choice(computador)
print('-=--' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--' * 15)
n = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if n == zorteio:
    print('PARÁBENS! Você conseuguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(zorteio, n))