# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

def desconto():
    preço = float(input('Qua é o preço do produto? R$'))
    novo = preço - (preço * 5/100)
    print(f'O produto que custava R${preço}, a promoção com desconto de 5% vai custar R${novo}')


desconto()