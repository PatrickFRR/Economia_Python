#O país A tem Bens duráveis de $2.9 bilhões, Bens não duráveis de $ 2.3 bilhões,
# Serviços de $ 10.8 bilhões, Estrutura de $ 1.3 bilhões e
# Variação nos estoques de $ 0.1 bilhões. Qual é o valor em moeda local do PIB?
import pandas as pd

#Calculando o PIB pela ótica da produção
bd = float(input('Digite o total de Bens durávies: $ '))
bn = float(input('Digite o total de Bens não duráveis: $ '))
s = float(input('Digite o total de Serviços: $ '))
e = float(input('Digite o total de Estruturas $ '))
v = float(input('Digite o total da Variação nos estoques: $ '))

#calculando PIB
pib = bd + bn + s + e + v

#Criando um dicionário DataFrame
data = {
'Componentes': ['Bens duráveis', 'Bens não duráveis', 'Serviços', 'Estruturas', 'Variação nos estoques', 'PIB total'],
'Fornecedor': ['$ {}'.format(bd), '$ {}'.format(bn), '$ {}'.format(s), '$ {}'.format(e), '$ {}'.format(v), '$ {}'.format(pib)]
}
#Criando o DataFrame
df = pd.DataFrame(data, columns=['Componentes', 'Fornecedor'])
print(df)

print('O seu PIB, pela ótica da produção, foi de $ {:.1f} trilhões na moeda local.'.format(pib))