lar = float(input('Qual a largura da parede ?'))
alt = float(input('Qual a altura da parede?'))
area = lar*alt
lit = area/2
print('Para pintar a parede de {}m2, sera necessario {:.1f} litros de tinta' .format(area,lit))
