'''from math import sqrt
c1 = float(input('Comprimento do cateto oposto: '))
n1 = c1 ** 2
c2 = float(input('Comprimento do cateto adjacente: '))
n2 = c2 ** 2
n3 = sqrt(n1 + n2)
print('A hipotenusa vai medir: {}'.format(n3))'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
ch = math.hypot(co, ca)
print('A hopotenusa vai medir :{}'.format(ch))
