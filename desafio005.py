n1 = input('Digite um numero: ')
r = int(n1) + 1
s = int(n1) - 1
print('O seu numero digitado e \033[32m {} \033[m' .format(n1))
print('O numero sucessor ao numero digitado e\033[34m {} \033[m' .format(r))
print('O numero anterior ao numero digitado e \033[31m{}' .format(s))
#print('Analisando o valor {}, o seu antecessor e {} e o sucessor e {}'.format(n, (n-1), (n+1)))
