# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

n = str(input('Qual seu nome completo? '))
verificar = 'SILVA' in n.upper()
print(f'Seu nome tem Silva? {verificar}')