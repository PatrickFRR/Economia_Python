#O país A tem exportações de $20 bilhões, compras governamentais de $ 1.000 bilhões,
# investimentos de empresas de $ 50 bilhões, importações de $ 40 bilhões e
# gasto de consumo de $ 2.000 bilhões. Qual é o valor em dólar do PIB?
import pandas as pd
#Calculando o PIB pela ótica da demanda

c = float(input('Digite o total de despesas do consumo: $ '))
i = float(input('Digite o total de despesas de investimento: $ '))
g = float(input('Digite o total de despesas do governo: $ '))
x = float(input('Digite o total de exportações: $ '))
m = float(input('Digite o total de importações: $ '))
#calculando exportações líquidas
t = x - m
#calculando PIB
pib = c + i + g + t


#Criando um dicionário DataFrame
data = {
'Componentes do PIB': ['Consumo', 'Investimento', 'Governo', 'Exportações', 'Importações', 'PIB total'],
'Demanda': ['$ {}'.format(c), '$ {}'.format(i), '$ {}'.format(g), '$ {}'.format(x), '$ {}'.format(m), '$ {}'.format(pib)]
}
#Criando o DataFrame
df = pd.DataFrame(data, columns=['Componentes do PIB', 'Demanda'])
print(df)

print('O seu PIB, pela ótica da demanda, foi de $ {} na moeda local.'.format(pib))
