# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto auno: '))
lista = [a1, a2, a3, a4]

sorteio = choice(lista)
print(f'O aluno escolhido por Maria foi: {sorteio}')