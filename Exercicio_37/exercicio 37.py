numero = int(input('Digite um número: '))
basedec = int(input('Qual base de conversão você deseja? \n 1 - Biário \n 2 - Octal \n 3 - Hexadecimal \n '))

if basedec == 1:
    print("A coversão de {} para binario é : {}".format(numero, bin(numero)[2:]))
elif basedec == 2:
    print('A conversão de {} para octal é : {}'.format(numero, oct(numero)[2:]))
elif basedec == 3:
    print('A conversão de {} para hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Número inválido.')