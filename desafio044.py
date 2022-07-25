print('{:=^40}'.format('LOJAS FELIX'))
compras = float(input('Precos das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro / cheque')
print('[ 2 ] a vista cartao')
print('[ 3 ] 2x no cartao')
print('[ 4 ] 3x ou mais no cartao')
opcao = int(input('Qual e a opcao?'))
if opcao == 1:
    print('Sua compra de R$ {} vai custar R$ {}'.format(compras, compras - (compras / 100 * 10)))
elif opcao == 2:
    print('Sua compra de R$ {} vai custar R$ {}'.format(compras, compras - (compras /100 * 5)))
elif opcao == 3:
    print('Sua compra sera parcelada em 2x de {}'.format(compras / 2))
    print('Sua compra de R$ {} vai custar R$ {}'.format(compras, compras))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra sera parcelada em {}x de {} com juros'.format(parcelas, ((compras / 100 * 20) + compras) / parcelas))
    print('Sua compra de R$ {} vai custar R$ {}'.format(compras, (compras / 100 * 20) + compras))
else:
    print('\033[31mOPCAO INVALIDA \n \033[mTente novamente')
