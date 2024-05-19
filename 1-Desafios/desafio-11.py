print('{:=^20}'.format('11'))

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = larg * alt

area_por_litro = 2
quantidade_de_tinta = area/area_por_litro

print('A sua parece tem a dimenção de {}x{} e sua área é de{}m².'.format(larg, alt, area))
print('Para pintar essa parece você precisará de {}l de tinta.'.format(quantidade_de_tinta))
