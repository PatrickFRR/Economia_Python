# Com base nas informações a seguir calcule o valor das exportações líquidas, o PIB e o PNL:
# Compras governamentais $120 bilhões, Depreciação $40 bilhões, Consumo	$400 bilhões,
# Investimento em negócios $60 bilhões, Exportações $100 bilhões, Importações $120 bilhões,
# Receita vinda do resto do mundo $10 bilhões e Pagamentos para o resto do mundo $8 bilhões.
import pandas as pd

#Calculando o PNL
c = float(input('Digite o total de consumo: $ '))
i = float(input('Digite o total de investimento: $ '))
g = float(input('Digite o total de compras do governo: $ '))
x = float(input('Digite o total de exportações: $ '))
m = float(input('Digite o total de importações: $ '))
rrm = float(input('Digite o total de receitas vinda do resto do mundo: $ '))
prm = float(input('Digite o total de pagamentos para o resto do mundo: $ '))
d = float(input('Digite o total de depreciação: $ '))
#calculando exportações líquidas
t = x - m
#calculando PIB
pib = c + i + g + t

#calculando o PNL
pnl = pib + rrm - prm - d

#Criando um dicionário DataFrame
data = {
'Componentes': ['Compras governamentais', 'Depreciação', 'Consumo', 'Investimento em negócios', 'Exportações', 'Importações', 'Receita vinda do resto do mundo', 'Pagamentos para o resto do mundo'],
'Valores em Bilhões': ['$ {}'.format(g), '$ {}'.format(d), '$ {}'.format(c), '$ {}'.format(i), '$ {}'.format(x), '$ {}'.format(m), '$ {}'.format(rrm), '$ {}'.format(prm)]
}
#Criando o DataFrame
df = pd.DataFrame(data, columns=['Componentes', 'Valores em Bilhões'])
print(df)
print('O valor das exportações líquidas é de ${:0f} bilhões na moeda local.'.format(t))
print('O seu PIB é de ${:0f} trilhões na moeda local.'.format(pib))
print('O seu PNL é de $ {:.0f} trilhões na moeda local.'.format(pnl))

