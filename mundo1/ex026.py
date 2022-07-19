f = str(input('Digite uma frase:')).upper().strip()
print('A letra A apareceu {} vezes na frase'.format(f.count('A')+1))
print('A primeira letra A apareceu na posição {}'.format(f.find('A')+1))
print('A ultima letra aparece na posição {}'.format(f.rfind('A')+1))