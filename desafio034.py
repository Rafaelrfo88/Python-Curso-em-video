salario = float(input('Qual e o salario do funcionario? R$ '))
if salario > 1250:
    print('Quem ganhava R$ {} passa a ganhar \033[31m R$ {} \033[m agora'.format(salario, ((salario / 100) * 10 ) + salario))
else:
    print('Quem ganhava R$ {} passa a ganhar \033[31mR$ {} \033[m agora'.format(salario, ((salario / 100) * 15) + salario))
'''
os comandos abaixo serve para fazer cores
\033[31m
\033[m  
'''
