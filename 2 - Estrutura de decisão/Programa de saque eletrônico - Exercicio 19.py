print('Bem vindo ao caixa eletrônico')
saque = int(input ('O valor do saque será de ' ))

n_100 = n_50 = n_10 = n_5 = n_1 = 0

n_100, saque = divmod(saque, 100)

n_50, saque = divmod(saque, 50)

n_10, saque = divmod(saque, 10)

n_5, saque = divmod(saque, 5)

n_1, saque = divmod(saque, 1)

if n_100 > 0:
    print(f'{n_100} nota(s) de 100')
if n_50 > 0:
    print(f'{n_50} nota(s) de 50')
if n_10 > 0:
    print(f'{n_10} nota(s) de 10')
if n_5 > 0:
    print(f'{n_5} nota(s) de 5')
if n_1 > 0:
    print(f'{n_1} nota(s) de 1')






