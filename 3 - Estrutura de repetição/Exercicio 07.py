maximo = float(input('Digite um numero: '))

for _ in range(4):
  maximo = max(maximo, float(input('Digite um numero: ')))
  print(f'O numero maximo encontrado até agora é {maximo}')
