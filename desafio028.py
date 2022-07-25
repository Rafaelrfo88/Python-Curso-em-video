from random import randint
from time import sleep
print('--=--=' * 10)
print('Vou pensa em um numero entre 0 e 5. Tente advinhar ...')
print('--=--=' * 10)
computador = randint(0, 5)
nmaq = int(input('Que numero eu escolhi? '))
print('PROCESSANDO...')
sleep(3)
if computador == nmaq:
    print('Parabens, o meu numero tambem foi {}'.format(computador))
else:
    print('Ganhei, eu pensei no numero {} e nao no numero {}'.format(computador, nmaq))
