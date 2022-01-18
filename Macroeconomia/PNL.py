# Com base nas informações a seguir calcule o PNL(Produto Nacional Líquido):
# Compras governamentais $120 bilhões, Depreciação $40 bilhões, Consumo	$400 bilhões,
# Investimento em negócios $60 bilhões, Exportações $100 bilhões, Importações $120 bilhões,
# Receita vinda do resto do mundo $10 bilhões e Pagamentos para o resto do mundo $8 bilhões.


#Calculando o PNL
c = float(input('Digite o total de consumo: $ '))
i = float(input('Digite o total de investimento: $ '))
g = float(input('Digite o total de compras do governo: $ '))
x = float(input('Digite o total de exportações: $ '))
m = float(input('Digite o total de importações: $ '))
rm = float(input('Digite o total de receitas vinda do resto do mundo: $ '))
prm = float(input('Digite o total de pagamentos para o resto do mundo: $ '))
d = float(input('Digite o total de depreciação: $ '))
#calculando exportações líquidas
t = x - m
#calculando PIB
pib = c + i + g + t

#calculando o PNL
pnl = pib + rm - prm - d
print('O seu PIB é de ${:0f} e o seu PNL é de $ {:.0f} na moeda local.'.format(pib, pnl))


