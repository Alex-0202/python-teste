'''import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))'''

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca **2) **(1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))