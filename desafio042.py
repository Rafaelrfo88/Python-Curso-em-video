'''r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[31mPODEM FORMAR \033[m triangulo!')
if r1 == r2 and r1 == r3 and r2 == r3:
    print('Os segmentos acima \033[31mPODEM FORMAR \033[m triangulo e ele e \033[31m equilatero!')
elif r1 == r2 and r1 == r3 and r2 != r3 or r1 == r2 and r1 != r3 and r2 == r3 or r1 != r2 and r1 == r3 and r2 == r3:
    print('Os segmentos acima \033[31mPODEM FORMAR \033[m triangulo e ele e \033[31m isosceles!')
elif r1 != r2 and r1 != r3 and r2 != r3:
    print('Os segmentos acima \033[31mPODEM FORMAR \033[m triangulo e ele e \033[31m escaleno!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulos!')'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[31mPODEM FORMAR \033[m triangulo!' ,end=' ')
    if r1 == r2 == r3:
        print('\033[31mEQUILATERIO!')
    elif r1 != r2 != r3 != r1:
        print('\033[31mESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulos!')
    