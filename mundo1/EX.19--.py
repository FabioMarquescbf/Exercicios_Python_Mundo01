import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto auno: '))
lista = [a1, a2, a3, a4]

sorteio = random.choice(lista)
print(f'O aluno escolhido por Maria foi: {sorteio}')