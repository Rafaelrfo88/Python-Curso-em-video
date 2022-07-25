n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
n3 = (n1 + n2) / 2
if n3 < 5:
    print('Sua nota foi {}, ela e abaixo de 5, por tanto: REPROVADO'.format(n3))
elif n3 >= 5 and n3 < 6.9:
    print('Sua nota foi {}, ela esta entre 5 e 6.9, voce esta de RECUPERACAO'.format(n3))
elif n3 > 7:
    print('Sua nota foi {}, acima de 7, voce esta APROVADO'.format(n3))
