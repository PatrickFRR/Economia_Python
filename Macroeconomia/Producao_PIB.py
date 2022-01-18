#O país A tem Bens duráveis de $2.9 bilhões, Bens não duráveis de $ 2.3 bilhões,
# Serviços de $ 10.8 bilhões, Estrutura de $ 1.3 bilhões e
# Variação nos estoques de $ 0.1 bilhões. Qual é o valor em dólar do PIB?

#Calculando o PIB pela ótica da produção
bd = float(input('Digite o total de Bens durávies: $ '))
bn = float(input('Digite o total de Bens não duráveis: $ '))
s = float(input('Digite o total de Serviços: $ '))
e = float(input('Digite o total de Estruturas $ '))
v = float(input('Digite o total da Variação nos estoques: $ '))

#calculando PIB
pib = bd + bn + s + e + v

print('O seu PIB,  pela ótica da produção, foi de $ {:.1f} na moeda local.'.format(pib))