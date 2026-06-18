## escrever um progrma que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input('Digite uma distância em metros: '))
decimetros = medida * 10
centimetros = medida * 100
milimetros = medida * 1000
decametros = medida / 10
hectometros = medida / 100
quilometros = medida / 1000
hectares = medida / 10000
print(f'{medida} equivalem a {decimetros} decímetros')
print(f'{medida} equivalem a {centimetros} centímetros')
print(f'{medida} equivalem a {milimetros} milímetros')
print(f'{medida} equivalem a {decametros} decâmetros')
print(f'{medida} equivalem a {hectometros} hectômetros')
print(f'{medida} equivalem a {quilometros} quilômetros')
print(f'{medida} equivalem a {hectares} hectares')