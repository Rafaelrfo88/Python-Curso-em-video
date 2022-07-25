'''nu = str(input('Informe o seu numero:'))
print('Analisando o numero {}' .format(nu))
print('Unidade {}'.format(nu[3]))
print('Dezena {}'.format(nu[2]))
print('Centena {}'.format(nu[1]))
print('Milhar {}'.format(nu[0]))'''

nu = int(input('Informe o seu numero:'))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print('Analisando o numero {}' .format(nu))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
