casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual o salario do comprador: R$ '))
anos = float(input('Quantos anos de financiamento? '))
prest = casa / (anos * 12)
sal = salario/100*30
print('Para pegar uma casa de R$ {:.2f} em {:.2f} anos a prestacao sera de R$ {:.2f}'.format(casa, anos, prest))
if prest >= sal:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo pode ser CONCEDIDO!')
