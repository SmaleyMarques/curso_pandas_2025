# %%
import pandas as pd


# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]

valores_acima_50 = [x for x in pontos if x >= 50]
print(valores_acima_50)

# OU...

valores_acima_50 = []
filtro = []

for i in pontos:
    filtro.append(i>=50)

resultado = []

for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

print(resultado)
# %%

df_filtro = pd.DataFrame(
    {
        "nome": ['Smaley', 'Jeniffer', 'Evelyn', 'Kevin'],
        "idade": [32, 31, 12, 5],
        "cidades_n": ['SGN', 'NLP', 'RJN', 'RJN']
    }
)

filtro = df_filtro["idade"] > 18

df_filtro[filtro]
#%%

df = pd.read_csv("../data/transacoes.csv")

# FILTRANDO PONTOS > 50

filtro = df["qtdePontos"] >= 50
df[filtro]

# %%

# FILTRANDO PONTOS > 50 E < 100 USANDO OPERADOR "&"

filtro = (df["qtdePontos"] >= 50) & (df["qtdePontos"] <= 100) 
# filtro = (df["qtdePontos"] >= 50) * (df["qtdePontos"] <= 100) 
df[filtro]


# %%

# FILTRANDO PONTOS = 1 OU PONTOS = 100 USANDO OPERADOR "|"

filtro = (df["qtdePontos"] >= 50) | (df["qtdePontos"] <= 100)
# filtro = (df["qtdePontos"] >= 50) + (df["qtdePontos"] <= 100)
df[filtro]
# %%

# FILTRANDO PONTOS > 0 E < 50, E DATA >=2025 USANDO OPERADOR "|"

filtro = (df["qtdePontos"] > 0) & (df["qtdePontos"] < 50) & (df["dtCriacao"] >= '2025-01-01')
# filtro = (df["qtdePontos"] > 0) * (df["qtdePontos"] < 50) * (df["dtCriacao"] >= '2025-01-01')
df[filtro]
# %%

# FILTRANDO PONTOS > 0 E < 50, OU DATA >=2025 USANDO OPERADOR "|"

filtro = (df["qtdePontos"] > 0) & (df["qtdePontos"] < 50) | (df["dtCriacao"] >= '2025-01-01')
# filtro = (df["qtdePontos"] > 0) * (df["qtdePontos"] < 50) + (df["dtCriacao"] >= '2025-01-01')
df[filtro]

# %%

# Usando método '.isin' e passando uma lista

df_novo =pd.read_csv("../data/transacao_produto.csv")

# filtro = (df_novo['idProduto'] == 1) | (df_novo['idProduto'] == 5)
filtro = df_novo['idProduto'].isin([1,5])
df_novo[filtro]

# %%

# Usando método '.notna' 

df_novo2 =pd.read_csv("../data/clientes.csv")

# filtro = ~df_novo2['dtCriacao'].isna()
filtro = df_novo2['dtCriacao'].notna()
df_novo2[filtro]