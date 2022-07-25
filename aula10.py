n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))
m = (n1+n2) / 2
print('A sua media foi {:.1f}'.format(m))
if m <= 7:
    print('Reprovado')
else:
    print('Aprovado')
