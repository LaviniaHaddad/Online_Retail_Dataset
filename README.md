Análise de Dados do Online Retail Dataset

Este projeto apresenta uma análise exploratória e limpeza do conjunto de dados Online Retail, que contém mais de 500 mil registros de vendas internacionais. Além disso, desenvolvi uma aplicação interativa usando Streamlit para facilitar a visualização e exploração dos dados.

📚 Sobre o Dataset

O dataset reúne registros de transações de uma loja de varejo online do Reino Unido, contendo informações como produtos vendidos, quantidades, clientes, preços, datas e países de origem.

⚙️ Passo a Passo do Projeto
Importação dos dados

Carregamento do dataset original a partir do arquivo CSV local (online_retail_cleaned.csv).

Limpeza dos dados

Remoção de valores ausentes importantes (CustomerID, Description).

Correção de valores inválidos, como quantidades negativas (indicando devoluções).

Criação da coluna booleana Devolucao para identificar vendas devolvidas.

Análises realizadas

Resumo estatístico das colunas numéricas.

Comparação entre vendas e devoluções, incluindo percentuais e gráfico de pizza.

Identificação dos principais países e produtos por volume de vendas (gráficos de barras horizontais e verticais).

Análise da evolução mensal das vendas (gráfico de linhas).

Visualização interativa com Streamlit

Aplicação com filtros dinâmicos por país, período e produto.

Gráficos interativos construídos com a biblioteca Plotly para melhor experiência.


📦 Estrutura do repositório
online_retail_cleaned.csv — Dataset limpo utilizado no projeto

app.py — Aplicação Streamlit para visualização interativa

README.md — Documentação do projeto

Outros scripts Python para análises específicas

🛠️ Tecnologias usadas
Python 3.x

Pandas

Streamlit

Plotly

