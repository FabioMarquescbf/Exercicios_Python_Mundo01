import math

a = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))

print(f'O âgulo de {a} tem o SENO de {seno:.2f}')
print(f'O Ângulo de {a} tem o COSSENO de {cosseno:.2f}')
print(f'O Ângulo de {a} tem a TANGENTE de {tangente:.2f}')