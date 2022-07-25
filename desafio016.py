#como usamos apenas uma funcao do math usamos apenas um modulo que e o trunc que ser para pegar a parte inteira
from math import trunc
i = float(input('Digite um valor: '))
n = trunc(i)
print('O valor digitado foi {} e a sua porcao inteira e {}'.format(i, n))
