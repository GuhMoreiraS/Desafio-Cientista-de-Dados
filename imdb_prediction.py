import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Carregar o dataset
df = pd.read_csv("/home/ubuntu/upload/desafio_indicium_imdb.csv")

# Pré-processamento de dados
df.drop(columns=["Unnamed: 0"], inplace=True)

# Converter 'Released_Year' para numérico, tratando erros
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")

# Converter 'Runtime' para numérico
df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(int)

# Converter 'Gross' para numérico, tratando valores ausentes e vírgulas
df["Gross"] = df["Gross"].str.replace(",", "").astype(float)
df["Gross"].fillna(df["Gross"].median(), inplace=True)

# Preencher valores ausentes de 'Meta_score' com a média
df["Meta_score"].fillna(df["Meta_score"].mean(), inplace=True)

# Seleção de variáveis para o modelo
# Variáveis numéricas: Runtime, Meta_score, No_of_Votes, Gross
# Variáveis categóricas: Genre, Director, Star1, Star2, Star3, Star4, Certificate, Released_Year

# Tratar Released_Year como categórica para one-hot encoding, preenchendo NaNs com um valor 'Desconhecido'
df['Released_Year'] = df['Released_Year'].fillna('Unknown').astype(str)

# Limitar o número de categorias para one-hot encoding para evitar muitas colunas
# Para Director e Stars, vamos pegar os top N e agrupar o restante como 'Other'
top_n_directors = 50
top_n_stars = 20 # Para cada Star1, Star2, Star3, Star4

# Directors
df['Director_processed'] = df['Director'].apply(lambda x: x if x in df['Director'].value_counts().head(top_n_directors).index else 'Other')

# Stars
for i in range(1, 5):
    star_col = f'Star{i}'
    df[f'{star_col}_processed'] = df[star_col].apply(lambda x: x if x in df[star_col].value_counts().head(top_n_stars).index else 'Other')

# One-Hot Encoding para as variáveis categóricas selecionadas e processadas
df_processed = pd.get_dummies(df, columns=[
    "Genre", "Director_processed", "Star1_processed", "Star2_processed", "Star3_processed", "Star4_processed", "Certificate", "Released_Year"
], dummy_na=False)

# Definir X (features) e y (target)
# Remover as colunas originais de Director e Stars, e outras colunas não usadas
X = df_processed.drop(columns=["IMDB_Rating", "Series_Title", "Overview", "Director", "Star1", "Star2", "Star3", "Star4"])
y = df_processed["IMDB_Rating"]

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliar o modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R-squared (R2): {r2:.4f}")

# Salvar o modelo
joblib.dump(model, "imdb_rating_predictor.pkl")
print("Modelo salvo como imdb_rating_predictor.pkl")

# Previsão para o filme específico
# Criar um DataFrame com as características do filme de exemplo
example_movie = {
    "Series_Title": "The Shawshank Redemption",
    "Released_Year": 1994,
    "Certificate": "A",
    "Runtime": 142,
    "Genre": "Drama",
    "Overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    "Meta_score": 80.0,
    "Director": "Frank Darabont",
    "Star1": "Tim Robbins",
    "Star2": "Morgan Freeman",
    "Star3": "Bob Gunton",
    "Star4": "William Sadler",
    "No_of_Votes": 2343110,
    "Gross": 28341469.0
}

example_df = pd.DataFrame([example_movie])

# Pré-processar o filme de exemplo da mesma forma que o dataset de treino
# É crucial que as colunas sejam as mesmas e na mesma ordem

# Aplicar o mesmo processamento de 'Other' para o filme de exemplo
example_df['Director_processed'] = example_df['Director'].apply(lambda x: x if x in df['Director'].value_counts().head(top_n_directors).index else 'Other')
for i in range(1, 5):
    star_col = f'Star{i}'
    example_df[f'{star_col}_processed'] = example_df[star_col].apply(lambda x: x if x in df[star_col].value_counts().head(top_n_stars).index else 'Other')

# Aplicar One-Hot Encoding ao filme de exemplo
example_processed = pd.get_dummies(example_df, columns=[
    "Genre", "Director_processed", "Star1_processed", "Star2_processed", "Star3_processed", "Star4_processed", "Certificate", "Released_Year"
], dummy_na=False)

# Garantir que o DataFrame de exemplo tenha as mesmas colunas que X_train
# Adicionar colunas que estão em X_train mas não em example_processed (preencher com 0)
missing_cols = set(X_train.columns) - set(example_processed.columns)
for c in missing_cols:
    example_processed[c] = 0

# Remover colunas que estão em example_processed mas não em X_train (se houver)
extra_cols = set(example_processed.columns) - set(X_train.columns)
example_processed.drop(columns=list(extra_cols), inplace=True)

# Reordenar as colunas para que fiquem na mesma ordem que X_train
example_processed = example_processed[X_train.columns]

# Fazer a previsão
predicted_imdb_rating = model.predict(example_processed)
print(f"\nNota do IMDB prevista para o filme de exemplo: {predicted_imdb_rating[0]:.2f}")


