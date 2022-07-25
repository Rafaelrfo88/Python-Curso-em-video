nome = str(input('Digite o seu nome completo: ')).strip()
#ta tirando os espacos em brancos da frase nome
print('Analisando seu nome...')
print('Seu nome em maiusculo fica: {}' .format(nome.upper()))
print('Seu nome em minusculo fica: {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
#no comando acima estamos tirando os espacos em branco com o comando -nome.cout(' '),
# no espaco em branco podemos usar qualquer coisa
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome e {} e ele tem {} letras' .format(separa[0], len(separa[0])))
