# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print(f'com R${real:.2f} você pode comprar US${dolar:.2f}')