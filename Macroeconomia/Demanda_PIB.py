#O país A tem exportações de $20 bilhões, compras governamentais de $ 1.000 bilhões,
# investimentos de empresas de $ 50 bilhões, importações de $ 40 bilhões e
# gasto de consumo de $ 2.000 bilhões. Qual é o valor em dólar do PIB?

#Calculando o PIB pela ótica da demanda
c = float(input('Digite o total de despesas do consumidor ou consumo: $ '))
i = float(input('Digite o total de despesas de negócios ou investimento: $ '))
g = float(input('Digite o total de despesas do governo em bens e serviços: $ '))
x = float(input('Digite o total de exportações: $ '))
m = float(input('Digite o total de importações: $ '))
#calculando exportações líquidas
t = x - m
#calculando PIB
pib = c + i + g + t

print('O seu PIB,  pela ótica da demanda, foi de $ {} na moeda local.'.format(pib))
