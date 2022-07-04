import pandas as pd


# Passo a passo de solução

# Abrir os 6 arquivos em Excell
lista_meses= ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas= pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No Mês {mes} Alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

# Para cada arquivo:


# Verificar se algum valor na coluna vendas é maior que 55.000

# Se for maior que 55.000 -> Envia um SMM com o Nome, o Mês e as vendas do vendedor

# Caso não seja maior que 55.000 não fazer nada 