al = float(input('Qual a sua altura: '))
pe = float(input('Qual o seu peso: '))
total = pe / (al ** 2)
if total < 18.5:
    print('Seu imc e {:.1f} \n \033[31mAbaixo do peso'.format(total))
elif total >= 18.5 and total < 25:
    print('Seu imc e {:.1f} \n \033[31mPeso ideal'.format(total))
elif total >= 25 and total < 30:
    print('Seu imc e {:.1f} \n \033[31mSobrepeso'.format(total))
elif total >= 30 and total < 40:
    print('Seu imc e {:.1f} \n \033[31mObesidade'.format(total))
elif total >= 40:
    print('Seu imc e {:.1f} \n \033[31mObesidade morbida'.format(total))
