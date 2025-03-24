# %%

import pandas as pd

df = pd.read_csv("./cartao.csv", sep=';')
df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])
df['vlParcela'] = df['vlVenda'] / df['qtParcelas']
df['ordemParcela'] = df['qtParcelas'].apply(lambda x: [i + 1 for i in range(x)])

# %%
df_explode = df.explode('ordemParcela', ignore_index=True)


def calcDtParcela(row):
    dt = row['dtTransacao'] + pd.DateOffset(months=row['ordemParcela'])
    dt = f"{dt.year}-{dt.month:02}"
    return dt

df_explode['dtParcela'] = df_explode.apply(calcDtParcela, axis= 1)
df_explode

# %%

(df_explode.groupby(['idCliente', 'dtParcela'])
                    ['vlParcela'].sum()
                    .reset_index()
)