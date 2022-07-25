n1 = input('Digite um numero:')
n2 = input('Digite mais um numero:')
s = n1 + n2
print('Os numeros', n1, '+', n2,  'juntados formam:', s)

# da maneira acima esta juntando os numeros, da maneira abaixo esta somando

n3 = int(input('Digite um numero:'))
n4 = int(input('Digite mais um numero:'))
p = n3 + n4
# print('A soma dos numeros', n3, '+', n4,  'resultam:', p)
print('A soma entre {} e {} vale {}'.format(n3, n4, p))
