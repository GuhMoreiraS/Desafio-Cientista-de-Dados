
## Análise Exploratória de Dados (EDA) - IMDB Filmes

### 1. Distribuição das Notas do IMDB

O histograma `imdb_rating_distribution.png` mostra a distribuição das notas do IMDB. Observa-se que a maioria dos filmes no dataset possui notas entre 7.6 e 8.2, com picos em torno de 7.7-7.8 e 8.0-8.1. A distribuição parece ser ligeiramente assimétrica à esquerda, indicando que há mais filmes com notas mais altas do que com notas muito baixas. Isso pode sugerir que o dataset contém predominantemente filmes bem avaliados, ou que filmes com notas muito baixas são menos representados.

### 2. Relação entre IMDB_Rating e Faturamento (Gross)

O gráfico de dispersão `imdb_rating_gross_scatterplot.png` explora a relação entre a nota do IMDB e o faturamento bruto dos filmes. Não há uma correlação linear forte e óbvia entre as duas variáveis. Embora existam alguns filmes com notas altas que também possuem faturamentos elevados, há uma grande dispersão, com muitos filmes de notas variadas apresentando faturamentos baixos ou médios. Isso sugere que a nota do IMDB, por si só, não é o único ou o principal fator determinante do sucesso financeiro de um filme.

### 3. Número de Filmes por Gênero

O gráfico de barras `movies_by_genre_countplot.png` ilustra a contagem de filmes por gênero. É visível que o gênero 'Drama' é o mais frequente no dataset, seguido por 'Action', 'Comedy', e 'Crime'. Isso indica que esses gêneros são populares ou que o dataset tem uma representação maior desses tipos de filmes. A diversidade de gêneros é grande, mas alguns gêneros são muito mais representados que outros.

### 4. Top 10 Diretores por Número de Filmes

O gráfico de barras `top_directors_countplot.png` exibe os 10 diretores com o maior número de filmes no dataset. Alfred Hitchcock e Steven Spielberg lideram a lista, o que sugere que eles são diretores prolíficos e/ou que seus filmes são bem representados na base de dados. A presença de diretores renomados como Martin Scorsese, Stanley Kubrick e Quentin Tarantino indica a qualidade geral dos filmes no dataset.

### 5. Matriz de Correlação de Variáveis Numéricas

O mapa de calor `correlation_heatmap.png` mostra as correlações entre as variáveis numéricas: `Released_Year`, `Runtime`, `IMDB_Rating`, `Meta_score`, `No_of_Votes` e `Gross`. 

Algumas observações:
- `IMDB_Rating` tem uma correlação positiva moderada com `No_of_Votes` (0.48) e `Meta_score` (0.26). Isso é esperado, pois filmes com mais votos e maior pontuação de crítica tendem a ter notas IMDB mais altas.
- `Gross` (faturamento) tem uma correlação positiva com `No_of_Votes` (0.60), indicando que filmes com maior número de votos tendem a ter maior faturamento. Isso faz sentido, pois filmes populares (com muitos votos) geralmente atraem mais público e, consequentemente, geram mais receita.
- `Runtime` (duração) tem uma correlação positiva fraca com `IMDB_Rating` (0.24) e `Gross` (0.14), sugerindo que filmes mais longos podem ter notas ligeiramente maiores e faturar um pouco mais, mas não é uma relação forte.
- `Released_Year` (ano de lançamento) tem correlações negativas fracas com `IMDB_Rating` (-0.13) e `Meta_score` (-0.29), o que pode indicar uma leve tendência de filmes mais antigos terem notas e meta-scores ligeiramente mais altos neste dataset, ou que a percepção de filmes clássicos é mais positiva ao longo do tempo.

### Hipóteses Iniciais:

1.  **Popularidade e Faturamento:** O número de votos (`No_of_Votes`) é um forte indicador de popularidade e está positivamente correlacionado com o faturamento (`Gross`). Filmes que geram mais engajamento do público (mais votos) tendem a ter maior sucesso financeiro.
2.  **Qualidade e Avaliação:** `Meta_score` e `No_of_Votes` são bons preditores da `IMDB_Rating`. Filmes aclamados pela crítica e com grande base de fãs tendem a ter notas IMDB elevadas.
3.  **Gênero e Sucesso:** Gêneros como 'Drama' e 'Action' são os mais representados, o que pode indicar uma preferência do público ou uma maior produção desses tipos de filmes. Uma análise mais aprofundada seria necessária para determinar se esses gêneros também se correlacionam com maior faturamento ou notas IMDB.
4.  **Diretores de Sucesso:** Diretores renomados como Alfred Hitchcock e Steven Spielberg consistentemente produzem filmes bem avaliados e populares, o que pode ser um fator a ser considerado na produção de novos filmes.
5.  **Faturamento vs. Qualidade:** O faturamento não é diretamente proporcional à nota do IMDB. Outros fatores, como marketing, distribuição e apelo de massa, provavelmente desempenham um papel significativo no sucesso financeiro de um filme, independentemente de sua avaliação crítica ou de público no IMDB.




### Respostas às Perguntas Específicas

#### 2a. Qual filme você recomendaria para uma pessoa que você não conhece?

Para recomendar um filme a uma pessoa que não conheço, eu escolheria um filme com uma **nota IMDB alta** e um **grande número de votos**. Isso sugere que o filme é amplamente aclamado e apreciado por um público diversificado, minimizando o risco de não agradar a um gosto específico. 

Com base na análise exploratória, um filme que se encaixa nesse perfil é **"The Shawshank Redemption"** (Um Sonho de Liberdade), que possui uma das maiores notas IMDB e um número de votos extremamente elevado no dataset. É um drama com uma narrativa universal de esperança e redenção, o que o torna uma escolha segura e geralmente bem recebida.

Outras opções seriam filmes como **"The Godfather"** (O Poderoso Chefão) ou **"The Dark Knight"** (Batman: O Cavaleiro das Trevas), que também apresentam notas altas e grande popularidade.




#### 2b. Quais são os principais fatores que estão relacionados com alta expectativa de faturamento de um filme?

Com base na análise de correlação e na EDA, os principais fatores relacionados com alta expectativa de faturamento de um filme são:

1.  **Número de Votos (`No_of_Votes`):** Este é o fator com a correlação mais forte e positiva com o faturamento (`Gross`). Isso sugere que filmes que geram grande engajamento e são amplamente assistidos (resultando em muitos votos) tendem a ter um faturamento significativamente maior. É um indicativo de popularidade e alcance do filme.

2.  **Qualidade Percebida (IMDB_Rating e Meta_score):** Embora a correlação direta entre `IMDB_Rating` e `Gross` não seja linearmente forte, filmes com notas IMDB e Meta_score mais altas tendem a atrair mais público e, consequentemente, mais votos. Indiretamente, a qualidade percebida contribui para a popularidade e, por extensão, para o faturamento.

3.  **Diretor e Elenco:** Embora não quantificado diretamente na correlação numérica, a presença de diretores renomados (como os do Top 10) e atores populares (`Star1`, `Star2`, etc.) pode ser um fator crucial para atrair público e gerar faturamento. Filmes com nomes estabelecidos na indústria tendem a ter um apelo maior.

4.  **Gênero:** Certos gêneros, como Drama e Ação, são mais representados no dataset, o que pode indicar uma maior demanda ou produção. Uma análise mais aprofundada seria necessária para correlacionar gêneros específicos com faturamento, mas é provável que alguns gêneros tenham um potencial de mercado maior.

Em resumo, a popularidade (medida pelo número de votos) é o indicador mais direto de alto faturamento, e essa popularidade é influenciada pela qualidade do filme, pelo talento envolvido (diretores, atores) e, possivelmente, pelo gênero.




#### 2c. Quais insights podem ser tirados com a coluna Overview? É possível inferir o gênero do filme a partir dessa coluna?

A coluna `Overview` contém uma breve sinopse ou descrição do enredo de cada filme. A partir dela, podemos tirar os seguintes insights:

*   **Temas e Palavras-chave:** A análise do texto na coluna `Overview` pode revelar temas recorrentes, palavras-chave e conceitos que são comuns em diferentes filmes. Por exemplo, a presença de palavras como "crime", "detetive" ou "investigação" pode indicar um filme de suspense ou policial. Termos como "amor", "relacionamento" ou "família" podem apontar para um drama ou romance.
*   **Sentimento e Tom:** Técnicas de Análise de Sentimento (Sentiment Analysis) poderiam ser aplicadas para inferir o tom geral do filme (positivo, negativo, neutro) ou as emoções predominantes, o que pode estar indiretamente ligado ao gênero (e.g., comédias tendem a ter um tom mais positivo).
*   **Identificação de Subgêneros:** Além dos gêneros principais, a `Overview` pode ajudar a identificar subgêneros ou nichos específicos dentro de um gênero mais amplo. Por exemplo, dentro de "Drama", pode-se distinguir "Drama Histórico", "Drama Familiar", etc.

**É possível inferir o gênero do filme a partir dessa coluna?**

Sim, **é possível inferir o gênero do filme a partir da coluna `Overview`**, mas com um certo grau de complexidade e incerteza. Isso seria um problema de **classificação de texto** no campo de Processamento de Linguagem Natural (PLN).

Para fazer isso, seriam necessários os seguintes passos:

1.  **Pré-processamento de Texto:** Limpeza do texto (remover pontuações, números, caracteres especiais), tokenização (dividir o texto em palavras), remoção de stop words (palavras comuns como "o", "a", "de"), e lematização/stemming (reduzir palavras à sua forma base).
2.  **Vetorização de Texto:** Transformar o texto em representações numéricas que podem ser usadas por algoritmos de Machine Learning. Métodos comuns incluem TF-IDF (Term Frequency-Inverse Document Frequency) ou Word Embeddings (como Word2Vec, GloVe, ou embeddings de modelos mais avançados como BERT).
3.  **Treinamento de um Modelo de Classificação:** Utilizar um conjunto de dados onde o `Overview` e o `Genre` correspondente são conhecidos para treinar um modelo de Machine Learning (e.g., Naive Bayes, Support Vector Machines, Random Forest, ou redes neurais). O modelo aprenderia a mapear as características do texto na `Overview` para os gêneros correspondentes.
4.  **Avaliação do Modelo:** Testar a precisão do modelo em um conjunto de dados não visto para verificar quão bem ele consegue prever o gênero.

Embora seja tecnicamente possível, a precisão da inferência dependeria da qualidade e da diversidade dos dados de treinamento, da complexidade dos gêneros (alguns gêneros podem ter descrições muito semelhantes) e da eficácia das técnicas de PLN aplicadas. Filmes que se encaixam em múltiplos gêneros ou que possuem enredos muito originais poderiam ser mais difíceis de classificar com precisão apenas pela `Overview`.




### 3. Explicação do Modelo de Previsão da Nota do IMDB

#### Variáveis e Transformações Utilizadas

Para prever a nota do IMDB (`IMDB_Rating`), foram utilizadas as seguintes variáveis do dataset, com as respectivas transformações:

*   **Variáveis Numéricas:**
    *   `Runtime`: Convertida para tipo inteiro, removendo a string " min".
    *   `Meta_score`: Valores ausentes preenchidos com a média da coluna.
    *   `No_of_Votes`: Utilizada diretamente como numérica.
    *   `Gross`: Convertida para tipo float, removendo vírgulas e preenchendo valores ausentes com a mediana da coluna. A mediana foi escolhida para ser mais robusta a outliers no faturamento.

*   **Variáveis Categóricas (One-Hot Encoding):**
    *   `Genre`: Convertida usando One-Hot Encoding. Cada gênero se torna uma nova coluna binária.
    *   `Director`: Para lidar com a alta cardinalidade, foram selecionados os 50 diretores mais frequentes. Diretores menos frequentes foram agrupados na categoria 'Other'. Em seguida, aplicada One-Hot Encoding.
    *   `Star1`, `Star2`, `Star3`, `Star4`: Similar aos diretores, para cada coluna de ator, foram selecionados os 20 atores mais frequentes, e o restante agrupado em 'Other'. Em seguida, aplicada One-Hot Encoding para cada uma.
    *   `Certificate`: Convertida usando One-Hot Encoding.
    *   `Released_Year`: Convertida para string e tratada como categórica para One-Hot Encoding, preenchendo NaNs com 'Unknown'. Isso permite capturar efeitos de ano de lançamento sem assumir uma relação linear.

As colunas `Series_Title` e `Overview` foram removidas do conjunto de features, pois `Series_Title` é um identificador único e `Overview` exigiria processamento de linguagem natural mais complexo, que está além do escopo inicial deste modelo preditivo.

#### Tipo de Problema

Estamos resolvendo um problema de **Regressão**. O objetivo é prever um valor contínuo (a nota do IMDB, que varia de 1.0 a 10.0), e não uma categoria discreta (classificação) ou um grupo (clusterização).

#### Modelo Escolhido: Random Forest Regressor

O modelo escolhido para a previsão foi o **Random Forest Regressor**.

*   **Prós:**
    *   **Alta Precisão:** Random Forests são conhecidos por sua alta precisão e bom desempenho em uma variedade de problemas de regressão e classificação.
    *   **Robustez a Outliers e Ruído:** São menos sensíveis a outliers e ruídos nos dados em comparação com outros modelos.
    *   **Lida com Não-Linearidades:** Consegue capturar relações não-lineares entre as features e o target.
    *   **Não Requer Escalonamento de Features:** Não é necessário escalar as features numéricas, o que simplifica o pré-processamento.
    *   **Importância de Features:** Permite avaliar a importância de cada feature na previsão, o que pode fornecer insights adicionais sobre quais fatores mais influenciam a nota do IMDB.

*   **Contras:**
    *   **Complexidade e Interpretabilidade:** Modelos de Random Forest são "caixas pretas" em certa medida. Embora forneçam importância de features, a lógica interna de cada árvore e a combinação delas podem ser difíceis de interpretar diretamente.
    *   **Custo Computacional:** Podem ser computacionalmente caros e demorados para treinar em datasets muito grandes, devido à construção de múltiplas árvores.
    *   **Overfitting (Potencial):** Embora menos propenso que árvores de decisão individuais, ainda há um risco de overfitting se o número de árvores (`n_estimators`) for muito alto ou se a profundidade das árvores não for controlada.

#### Medida de Performance do Modelo

Para avaliar o desempenho do modelo, foram utilizadas duas métricas:

1.  **Mean Squared Error (MSE - Erro Quadrático Médio):**
    *   **Por que escolhida:** O MSE mede a média dos quadrados dos erros, ou seja, a diferença quadrática média entre os valores previstos e os valores reais. É uma métrica comum para problemas de regressão e penaliza erros maiores de forma mais significativa. Um MSE menor indica um modelo com melhor desempenho.

2.  **R-squared (R2 - Coeficiente de Determinação):**
    *   **Por que escolhida:** O R2 indica a proporção da variância na variável dependente que é previsível a partir das variáveis independentes. Ele varia de 0 a 1 (ou pode ser negativo para modelos muito ruins). Um R2 de 1 indica que o modelo explica toda a variabilidade da variável resposta, enquanto um R2 de 0 indica que o modelo não explica nenhuma variabilidade. É uma métrica intuitiva que fornece uma ideia da "bondade do ajuste" do modelo.

Ambas as métricas são complementares. O MSE dá uma ideia da magnitude do erro, enquanto o R2 fornece uma perspectiva sobre o quanto da variância dos dados o modelo consegue explicar.

#### Previsão para o Filme de Exemplo

Para o filme com as características fornecidas:

```json
{
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': '1994',
    'Certificate': 'A',
    'Runtime': '142 min',
    'Genre': 'Drama',
    'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
    'Meta_score': 80.0,
    'Director': 'Frank Darabont',
    'Star1': 'Tim Robbins',
    'Star2': 'Morgan Freeman',
    'Star3': 'Bob Gunton',
    'Star4': 'William Sadler',
    'No_of_Votes': 2343110,
    'Gross': '28,341,469'
}
```

A nota do IMDB prevista pelo modelo foi de **8.75**.


