# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Estudo: Metodos.

# objeto.
algo = input('Digite algo, para mostrar suas informações: ')

# tipo
# Sempre será (str), pois o (input) sempre retorna como (string).
def tipo(algo):
    tipo = type(algo)
    print(f'O tipo primitivo desse valor é {tipo}')

# espaço.
def espaço(algo):
    print('So tem espaços', algo.isspace())

# numero.
def numerico(algo):
    print('É um número?', algo.isnumeric())

# alfabetico.
def alfabetico(algo):
    print('É alfabético?', algo.isalpha())

# alfanúmerico.
def alfanumerico(algo):
    print('É alfanúmerico?', algo.isalnum())

# maiúscula
def maiuscula(algo):
    print('Está em maiúscula?', algo.isupper())

# minúscula
def minuscula(algo):
    print('Está em minuscula?', algo.islower())

# capitalizada
def capitalizada(algo):
    print('Está em capitalizada?', algo.istitle())

tipo(algo)
espaço(algo)
numerico(algo)
alfabetico(algo)
alfanumerico(algo)
maiuscula(algo)
minuscula(algo)
capitalizada(algo)




