while True:
    try:
        numero = int(input('O numero informado é: '))
    except ValueError:
        print('Deve ser fornecido um valor inteiro')
    else:
        if 0<= numero <= 10:
            print(f'O numero informado foi {numero} ')
            break
        else:
            print('O numero informado deve ser válido')