from random import randint
from time import sleep
print('Sua opcao:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jogador = int(input('Qual e a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if jogador == computador:
    print('Empate')
elif jogador == 0 and computador == 1:
    print('Computador ganhou')
elif jogador == 0 and computador == 2:
    print('Voce ganhou')
elif jogador == 1 and computador == 0:
    print('Voce ganhou')
elif jogador == 1 and computador == 2:
    print('Computador ganhou')
elif jogador == 2 and computador == 0:
    print('Computador ganhou')
elif jogador == 2 and computador == 1:
    print('Voce ganhou')
print('Jogador escolheu {} e o computador {}'.format(itens[jogador], itens[computador]))
   