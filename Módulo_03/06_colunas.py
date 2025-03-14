# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv")

print("Quantidade de linhas e colunas:", '\n', df.columns, '\n')

print("Informações gerais:", '\n', df.info(memory_usage= 'deep'), '\n')

print("Tipagem por colunas:", '\n', df.dtypes, '\n')
# %%
df = df.rename(columns={"qtdePontos": "Pontos"}) # recebe um dicionário contendo antes/depois para nome da coluna

df.rename(columns={"descSistemaOrigem": "SistemaOrigem"}, inplace=True) # inplace anula necessidade de reatribuição

df
# %%
df['idCliente'] # retorna uma series

df[['idCliente']] # retorna um df de uma coluna

df[['idCliente', 'Pontos']] # retorna um df de mais de uma coluna
# %%

# Ordenando colunas

colunas = df.columns.to_list()
colunas.sort()

df[colunas]
