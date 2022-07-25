#Aluguel de carros
d = int(input('Quantos dias alugados? '))
d1 = d * 60
k = float(input('Quantos Km rodados? '))
k1 = k * 0.15
t = d1 + k1
print('O valor a pagar e de R${:.2f}'.format(t))
