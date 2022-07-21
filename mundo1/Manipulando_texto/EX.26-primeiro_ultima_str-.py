# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”.
# e em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
# quantidade.
quant = frase.count('A')
print(f'A letra A apareceu {quant} vezes na frase')

# primeira posição.
pri_posi = frase.find('A')+1
print(f'A primeira letra A apareceu na posição {pri_posi}')

# ultima posição..format(
ult_posi = frase.rfind('A')+1
print(f'A ultima letra aparece na posição {ult_posi}')

# Nessas Funções, sempre tem que se passar os Parametros. - EX: variavel.count('Parametro')