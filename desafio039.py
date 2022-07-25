from datetime import date
ano = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = atual - ano
anos = ano + 18
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento sera em {}'.format(anos))
elif idade > 18:
    print('Voce ja deveria ter se alistado ha {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(anos))
elif idade == 18:
    print('Voce devera se apresentar nesse ano de {}'.format(atual))
