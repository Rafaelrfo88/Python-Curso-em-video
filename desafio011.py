#Faca um programa que leia a largura e a altura de uma parede em metros. Calcule a sua area e a quantidade de tinta
#necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2 metros quadrados
a = float(input('Qual a altura da sua parede: '))
l = float(input('Qual a largura da sua parede: '))
t = a * l
print('Sua parede tem a dimensao de {} x {} e sua area e de {}m²' .format(a, l, t))
tin = t / 2
print('Para pintar essa parede, voce precisara de {}l de tinta.' .format(tin))
