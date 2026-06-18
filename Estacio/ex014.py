largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura ## formula de calculo da área
tinta = area / 2 ## 2 equivale a quantidade de tinta necessária para pintar 1m² de parede
print('A área da parede é de {:.2f}m².'.format(area))
print('A quantidade de tinta necessária para pintar a parede é de {:.2f} litros.'.format(tinta))