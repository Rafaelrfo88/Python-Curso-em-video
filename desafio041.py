from datetime import date
ano = int(input('Em que ano o atleta nasceu? '))
atual = date.today().year
idade = atual - ano
if idade < 9:
    print('O atleta tem {} anos. \nClassificacao: \033[31mMIRIM'.format(idade))
elif idade >= 9 and idade < 14:
    print('O atleta tem {} anos. \nClassificacao: \033[31mINFANTIL'.format(idade))
elif idade >= 14 and idade < 19:
    print('O atleta tem {} anos. \nClassificacao: \033[31mJUNIOR'.format(idade))
elif idade >= 19 and idade < 25:
    print('O atleta tem {} anos. \nClassificacao: \033[31mSENIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos. \nClassificacao: \033[31mMASTER'.format(idade))
