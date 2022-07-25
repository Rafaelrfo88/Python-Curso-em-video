n1 = input('Digite um numero: ')
t = int(n1) * 3
r = int(n1) ** (1/2)
print('O dobro do seu numero digitado \033[32m {} \033[m e \033[31m{} \033[m' .format(n1, int(n1) * 2))
print('O triplo do seu numero digitado \033[32m {} e \033[33m{} \033[m' .format(n1, t))
print('A raiz quadrada do seu numero digitado \033[32m {} e \033[34m{} \033[m' .format(n1, r))
