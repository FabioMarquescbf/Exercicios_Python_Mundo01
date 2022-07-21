# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando:
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = float(input('Qual é a distancia da sua viagem? '))
print(f'Você esta prestes a começar uma viagem de {d}Km')
if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')

