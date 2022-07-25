nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('O seu primeiro nome e {}' .format(n[0]))
print('O seu ultimo nome e {}' .format(n[len(n)-1]))
print('O seu nome completo tem o total de {} letras ' .format(len(nome)-nome.count(' ')))
'''
o comando -nome.count(' ') esta tirando os espacos em branco 
'''
print('O seu nome completo tem {} nomes no total ' .format(len(n)))
print('A quantidade de letras no seu primeiro nome e {}' .format(len(n[0])))
