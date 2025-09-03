import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/home/ubuntu/upload/desafio_indicium_imdb.csv")

# Limpeza e transformação de dados
df.drop(columns=["Unnamed: 0"], inplace=True)
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(int)
df["Gross"] = df["Gross"].str.replace(",", "").astype(float)

# Tratamento de valores ausentes (exemplo: preencher com a média ou mediana)
df["Meta_score"].fillna(df["Meta_score"].mean(), inplace=True)
df["Gross"].fillna(df["Gross"].median(), inplace=True)

# Análise exploratória e visualizações

# Distribuição da nota do IMDB
plt.figure(figsize=(10, 6))
sns.histplot(df["IMDB_Rating"], kde=True)
plt.title("Distribuição das Notas do IMDB")
plt.xlabel("Nota do IMDB")
plt.ylabel("Frequência")
plt.savefig("imdb_rating_distribution.png")
plt.close()

# Relação entre IMDB_Rating e Gross
plt.figure(figsize=(10, 6))
sns.scatterplot(x="IMDB_Rating", y="Gross", data=df)
plt.title("IMDB Rating vs. Gross Revenue")
plt.xlabel("Nota do IMDB")
plt.ylabel("Faturamento (Gross)")
plt.savefig("imdb_rating_gross_scatterplot.png")
plt.close()

# Filmes por Gênero
plt.figure(figsize=(12, 7))
sns.countplot(y="Genre", data=df, order=df["Genre"].value_counts().index)
plt.title("Número de Filmes por Gênero")
plt.xlabel("Contagem")
plt.ylabel("Gênero")
plt.savefig("movies_by_genre_countplot.png")
plt.close()

# Top Diretores por número de filmes
plt.figure(figsize=(12, 7))
sns.countplot(y="Director", data=df, order=df["Director"].value_counts().head(10).index)
plt.title("Top 10 Diretores por Número de Filmes")
plt.xlabel("Contagem")
plt.ylabel("Diretor")
plt.savefig("top_directors_countplot.png")
plt.close()

# Correlação entre variáveis numéricas
plt.figure(figsize=(10, 8))
sns.heatmap(df.select_dtypes(include=["number"]).corr(), annot=True, cmap="coolwarm")
plt.title("Matriz de Correlação de Variáveis Numéricas")
plt.savefig("correlation_heatmap.png")
plt.close()

print("EDA completa concluída. Gráficos salvos como arquivos PNG.")


