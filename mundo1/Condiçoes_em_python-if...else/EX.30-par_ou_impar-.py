# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Me diga um número quaquer: '))
resultado = numero % 2
if resultado == 0:
    print(f'o número {numero} é par')
else:
    print(f'O número {numero} é impar')
