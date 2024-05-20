import math
angulo_graus = float(input('Digite o ângulo em graus: '))
angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print('O grau dígitado foi {} graus'.format(angulo_graus))
print('O valor de seno é {:.2f}'.format(seno))
print('O valor do cosseno é {:.2f}'.format(cosseno))
print('O valor da tangente é {:.2f}'.format(tangente))