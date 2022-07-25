from time import sleep
v1 = float(input('Qual e a velocidade atual do carro? '))
multa = (v1 % 80) * 7
if v1 <= 80:
    print('Tenha um bom dia, Dirija com seguranca')
else:
    print('\033[31m Multado \033[m, iremos calcular o valor da sua multa, aguarde ...')
    sleep(3)
    print('Voce esta acima da velocida, devera pagar uma multa de \033[31m R${:.2f} \033[m reais' .format(multa))
