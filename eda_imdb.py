import pandas as pd

df = pd.read_csv("/home/ubuntu/upload/desafio_indicium_imdb.csv")

print("Informações básicas do conjunto de dados:")
df.info()

print("\nPrimeiras 5 linhas do conjunto de dados:")
print(df.head())

print("\nEstatísticas descritivas do conjunto de dados:")
print(df.describe(include='all'))


