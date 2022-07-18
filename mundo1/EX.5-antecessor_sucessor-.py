# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número, para analizar seu antecessor e sucessor: '))
antecessor = numero - 1
sucessor = numero + 1
print(f'Analisando o valor {numero} -> seu antecessor é {antecessor} e seu sucessor é {sucessor}')