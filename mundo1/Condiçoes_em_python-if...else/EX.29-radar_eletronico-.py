# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.


carro = float(input('Qual a velocidade atual do carro? '))
if carro <80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! você excedeo o limete permito que é de 80Km/h')
    print('Você deve pagar uma multa de R$280.00!')
    print('Tenha um bom dia! Dirija com segurança!')