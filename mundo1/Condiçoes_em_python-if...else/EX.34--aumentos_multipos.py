# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o salário do funcionario? R$'))
mais15 = salario + (salario * 15/100)
mais10 = salario + (salario * 10/100)
if salario >= 1250:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${mais15:.2f} agora!')
else:
    print(f'quem ganhava R${salario:.2f} passa a ganhar R${mais10:.2f} agora!')