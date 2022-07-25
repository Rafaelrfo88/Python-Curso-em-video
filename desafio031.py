viagem = float(input('Qual e a distacia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {} km'.format(viagem))
if viagem <= 200:
    print('O preco da sua passagem sera de R$ {} reais'.format(viagem * 0.5))
else:
    print('O preco da sua passagem com desconto sera de R$ {} reais'.format(viagem * 0.45))
