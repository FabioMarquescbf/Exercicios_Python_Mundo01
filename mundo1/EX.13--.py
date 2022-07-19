salario = float(input('Qual é o salario do funcionário? R$'))
desconto = salario + (salario * 15/100)
print(f'Um funcionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${desconto:.2f}')