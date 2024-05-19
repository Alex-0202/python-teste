print('{:=^20}'.format('11'))

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = larg * alt

area_por_litro = 2
quantidade_de_tinta = area/area_por_litro

print('A área da parede de {} metro de altura e {} metros de largura é: {} metros quadrados'.format(alt, larg, area))
print ('A quantidade de tinta necessária é de {:.2f} litros'.format(quantidade_de_tinta))
