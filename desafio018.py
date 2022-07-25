import math
a1 = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(a1))
cosseno = math.cos(math.radians(a1))
tangente = math.tan(math.radians(a1))
print('No angulo de {} tem o SENO de {:.2f}'.format(a1, seno))
print('No angulo de {} tem o COSSENO de {:.2f}'.format(a1, cosseno))
print('No angulo de {} tem o TANGENTE de {:.2f}'.format(a1, tangente))

