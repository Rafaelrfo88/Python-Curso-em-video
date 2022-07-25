'''cit = str(input('Em que cidade voce nasceu: ')).strip()
sep = cit.split()
print('Santos' in sep[0])'''

cit = str(input('Em que cidade voce nasceu: ')).strip()
print(cit[:5].upper() == 'SANTO')
