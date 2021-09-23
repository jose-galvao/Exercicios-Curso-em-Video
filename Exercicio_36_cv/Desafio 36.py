valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Em quantos anos você vai pagar a casa?'))

prestacao = anos * 12
mensal = valorcasa / prestacao
porcentagem = (mensal * 100) / salario

if porcentagem <= 30:
    print('Você pode comprar a casa, sua parcela mensal será de {:.2f} reais.'.format(mensal))
else:
    print('você não pode comprar essa casa, por exceder o limite de 30% do seu salario mensal!')