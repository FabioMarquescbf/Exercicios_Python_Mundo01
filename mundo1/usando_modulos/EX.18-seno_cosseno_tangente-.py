# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

a = float(input('Digite o ângulo que você deseja: '))

def seno(a):
    seno = math.sin(math.radians(a))
    print(f'O ãngulo de {a} tem o SENO de {seno:.2f}')

def cosseno(a):
    cosseno = math.cos(math.radians(a))
    print(f'O ãngulo de {a} tem o COSSENO de {cosseno:.2f}')

def tangente(a):
    tangente = math.tan(math.radians(a))
    print(f'O ãngulo de {a} tem SENO de {tangente:.2f}')


seno(a)
cosseno(a)
tangente(a)