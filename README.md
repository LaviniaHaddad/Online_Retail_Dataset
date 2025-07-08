# Análise de Dados do Online Retail Dataset

Este projeto é uma análise exploratória e limpeza do conjunto de dados *Online Retail* com mais de 500 mil registros de vendas internacionais. Além disso, construí uma aplicação interativa usando **Streamlit** para visualização e exploração dos dados.

---

## 📚 Sobre o Dataset

O conjunto de dados contém registros de transações de uma loja de varejo online no Reino Unido, com informações sobre produtos, quantidades, clientes, preços, datas e países.

---

## ⚙️ Passo a Passo do Projeto

1. **Importação dos dados**  
   - Dataset original carregado a partir de arquivo CSV local (`online_retail_cleaned.csv`).

2. **Limpeza dos dados**  
   - Remoção de valores ausentes importantes (`CustomerID`, `Description`).  
   - Correção de valores inválidos (quantidade negativa, que indica devoluções).  
   - Criação de coluna booleana `Devolucao` para identificar devoluções.

3. **Análises realizadas**  
   - Resumo estatístico das colunas numéricas.  
   - Comparação entre vendas e devoluções, incluindo percentuais e gráfico de pizza.  
   - Top países e produtos por quantidade vendida (barras horizontais e verticais).  
   - Evolução mensal das vendas (gráfico de linha).

4. **Visualização interativa com Streamlit**  
   - App com filtros dinâmicos por país, período e produto.  
   - Visualização dos gráficos com a biblioteca Plotly para melhor interação.

---

## 🚀 Como usar o projeto

1. Clone este repositório:  
  
   git clone https://github.com/laviniahaddad/Online_Retail_Dataset.git
   

2. Instale as dependências:

   pip install -r requirements.txt

3. Execute o app Streamlit:

 Streamlit run app.py

4. Explore os filtros na barra lateral e visualize as análises.

📦 Estrutura do repositório
online_retail_cleaned.csv — Dataset limpo utilizado no projeto

app.py — Aplicação Streamlit para visualização interativa

README.md — Documentação do projeto

🛠️ Tecnologias usadas
Python 3.x

Pandas

Streamlit

Plotly