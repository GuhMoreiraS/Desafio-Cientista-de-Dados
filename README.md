# Desafio Indicium - Análise de Dados IMDB

Este repositório contém a solução para o desafio de Ciência de Dados proposto pela Indicium, que envolve a análise de um dataset de filmes do IMDB e a construção de um modelo preditivo para a nota do IMDB.

## Estrutura do Projeto

*   `desafio_indicium_imdb.csv`: O dataset original fornecido.
*   `[Lighthouse]DesafioCiênciadeDados2025-11.docx`: O documento com a descrição do desafio.
*   `eda_imdb.py`: Script Python para uma Análise Exploratória de Dados (EDA) inicial.
*   `eda_imdb_full.py`: Script Python para uma EDA mais completa, incluindo limpeza de dados e geração de visualizações.
*   `imdb_prediction.py`: Script Python para o desenvolvimento do modelo de previsão da nota do IMDB, incluindo pré-processamento, treinamento, avaliação e previsão para um filme de exemplo.
*   `imdb_rating_predictor.pkl`: O modelo de previsão treinado, salvo no formato .pkl.
*   `eda_report.md`: Relatório detalhado da EDA e das respostas às perguntas do desafio, em formato Markdown.
*   `eda_report.pdf`: Versão em PDF do relatório da EDA.
*   `requirements.txt`: Lista de todas as bibliotecas Python e suas versões utilizadas no projeto.

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2.  **Crie um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: .venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os scripts:**
    *   Para a EDA inicial:
        ```bash
        python3 eda_imdb.py
        ```
    *   Para a EDA completa e geração de gráficos:
        ```bash
        python3 eda_imdb_full.py
        ```
    *   Para treinar o modelo, salvar e fazer a previsão de exemplo:
        ```bash
        python3 imdb_prediction.py
        ```

Os resultados da EDA (gráficos) serão salvos como arquivos PNG no diretório raiz do projeto. O modelo treinado será salvo como `imdb_rating_predictor.pkl`.

## Relatórios e Análises

O arquivo `eda_report.md` (e sua versão em PDF `eda_report.pdf`) contém a análise detalhada dos dados, as respostas às perguntas propostas no desafio e a explicação do modelo de previsão da nota do IMDB.


