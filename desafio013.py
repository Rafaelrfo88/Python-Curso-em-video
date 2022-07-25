#faca um algoritmo que leia o salario de um funcionario e mostre o seu novo salario, com um aumento de 10% de aumento
n1 = float(input('Qual o salario do funcionario: R$ '))
t = (n1 / 100) * 10
ns = n1 + t
print('O novo salario do funcionario vai ser de : R$ {:.2f}' .format(ns))
