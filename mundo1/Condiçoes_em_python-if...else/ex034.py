salario = float(input('Qual é o salário do funcionario? R$'))
ganhar = salario + (salario * 15/100)
ganhar2 = salario + (salario * 10/100)
if salario >= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, ganhar2))
else:
    print('quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, ganhar ))