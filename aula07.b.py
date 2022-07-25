n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {},\n o produto e {},\n a divisao e {:.3f},\n'.format(s, m, d), end=' ')
print('Divisao inteira {} e potencia {}'.format(di, e))
