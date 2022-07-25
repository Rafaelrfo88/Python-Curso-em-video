numero = float(input('Me diga um numero qualquer:'))
if (numero % 2) == 0:
    print('Seu numero \033[31m {} \033[m  e \033[31m par'.format(numero))
else:
    print('Seu numero \033[33m {} \033[m  e \033[31m impar'.format(numero))
