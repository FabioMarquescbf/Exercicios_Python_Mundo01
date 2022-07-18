# Escreva um programa que leia um valor em metros e o exiba convertido.
# converter valor de metros em quilômetro, hectômetro, decâmetro, decímetro, centímetro, milímetro.

medida = float(input('Uma distância em metros: '))

print(f'A medida de {medida} corresponde a:')

def km(medida):
    km = medida / 1000
    print(km,'km')

def hm(medida):
    hm = medida / 100
    print(hm,'hm')

def dam(medida):
    dam = medida / 10
    print(dam,'dam')

def dm(medida):
    dm = medida * 10
    print(dm,'dm')

def cm(medida):
    cm = medida * 100
    print(cm,'cm')

def mm(medida):
    mm = medida * 1000
    print(mm,'mm')

km(medida)
hm(medida)
dam(medida)
dm(medida)
cm(medida)
mm(medida)