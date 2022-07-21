# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome comleto: ')).strip()  # - (.strip()) -> Elimina os Espaços iniciais. -

print('Analisando seu nome...')

print(f'Seu nome em maiúscula é {nome.upper()}')  # - (.upper) -> Deixa toda a string em (Maiscúlo). -
print(f'Seu nome em minúscula é {nome.lower()}')  # - (.lower) -> Deixa toda a sting em (Minúsculo). -

print(f'seu nome tem ao todo {len(nome) - nome.count(" ")} letras') 
 # - Para não contar os Espaços -> Contador de Comprimento(len) Menos Contado de Espaços(.count) -

print(f'Seu primeiro nome tem {nome.find(" ")} letras')
#  - (.find(" ")) -> Encontra o primeiro Espaço - EX: <Fábio Marques> O Primeiro Espaço esta na Posição 5. -  (Saída = 5)  - 
