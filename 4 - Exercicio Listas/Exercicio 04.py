notas = []

while True:
  entrada = input('Digite um numero: ')
  if entrada == '-1':
    break
  notas.append(float(entrada))

tamanho = len(notas)
print(f'O sistema leu {tamanho} notas') ## a - Quantidade de notas lidas
print(' '.join([str(nota) for nota in notas])) ## b - Quais as notas lidas
notas.reverse()

for nota in notas:
  print(nota)          ## c - Notas lidas verticalmente em ordem inversa

soma = sum(notas)
print(f'A soma das notas foi de {soma}') ## d - soma das notas

media = soma / tamanho
print(f'A media das notas foi de {media}') ## e - media das notas

print('Notas acima da média')
print(' '.join([str(nota) for nota in notas if nota > media ])) ## f - notas acima da média

print('Notas abaixo da média')
print(' '.join([str(nota) for nota in notas if nota < 7 ]))  ## e - notas abaixo da média

print('Fim das estatiscas.')