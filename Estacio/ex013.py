dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
dinheiro2 = float(input('E quantos dolares você tem? US$ '))
dolar = dinheiro / 5.06
real = dinheiro2 * 5.06
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(dinheiro, dolar))
print('E com US$ {:.2f} você pode comprar R$ {:.2f}'.format(dinheiro2, real))