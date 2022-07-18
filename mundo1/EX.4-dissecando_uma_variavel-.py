# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo, para saber seu tipo: ')
tipo = type(algo)

print(f'O tipo primitivo desse valor é {tipo}')

# numero.
def inteiro(algo):
    if tipo == int:
        print('é um número? True')
    else:
        print('é um número? False')

# alfabético.
def alfabetico(algo):
    if tipo == str:
        print('É alfabético? True')
    else:
        print('É alfabético? False')

# alfanúmerico.


# maiúscula
def maiuscula(algo):
    if algo == algo.upper():
        print('Está em maiúscula? True')
    else:
        print('Está em maiscúla? True')

# minúscula
def minuscula(algo):
    if algo == algo.lower():
        print('Está em minúscula? True')
    else:
        print('Está em minúscula? False')

# capitalizada
def capitalizada(algo):
    if algo == algo.title():
        print('Está capitalizada? True')
    else:
        print('Esá capitalizada? False')


inteiro(algo)
alfabetico(algo)
maiuscula(algo)
minuscula(algo)
capitalizada(algo)






