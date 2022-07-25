#Faca um algoritmo que leia o preco de um produto e mostre o novo preco, com 5% de desconto
n1 = float(input('Digite o valor do seu produto: R$ '))
t = (n1 /100) * 5
r = n1 - t
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}' .format(n1, r))
