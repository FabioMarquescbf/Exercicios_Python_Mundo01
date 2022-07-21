# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número para analizar seu dobro, triplo e a raiz quadrada: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2)
print(f'O dobro de {numero} vale {dobro}.')
print(f'O triple de {numero} vale {triplo}.')
print(f'A raiz quadrada de {numero} valor {raiz:.2f}.')