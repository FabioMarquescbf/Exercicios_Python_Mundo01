# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5.
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('-~' * 30)
print('Vou Pensar em um número entre 0 e 5, Tente adivinhar...')
print('-~' * 30)

from random import choice
from time import sleep

dado = list([1, 2, 3, 4, 5])
sorteio = choice(dado)

chute = int(input('Em que número eu pensei? '))
print('PROCESSANDO..')
sleep(0.5)
if chute == dado:
    print('PARABÉNS! Você consegui me vencer!')
else:
    print(f'GANHEI! Pensei no número {sorteio} não no {chute}')
