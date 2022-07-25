#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considere US$1.00 = R$3,27
n1 = float(input('Quanto de dinheiro vc tem em sua carteira? R$'))
t = n1 / 3.27
print('Com R${:.2f} reais voce pode comprar US${:.2f} de dolar' .format(n1, t))
