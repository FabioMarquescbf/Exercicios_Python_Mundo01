dia = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodadados?'))
pago = (dia * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')

