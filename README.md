# 🛍️ Análise de Dados – Online Retail Dataset

Este projeto aborda a **limpeza**, **análise exploratória** e **visualização interativa** de dados de vendas online com mais de 500 mil registros. Usei **Python**, **SQL** e **Streamlit** para criar insights dinâmicos e profissionais.

---

## 📚 Sobre o Dataset

O dataset contém transações de uma loja de varejo online no Reino Unido, incluindo:

- Produtos vendidos  
- Quantidades  
- Preços unitários  
- Datas das transações  
- Identificadores de clientes  
- Países de origem  

---

## ⚙️ Etapas do Projeto

### 🔹 1. Importação dos dados  
- Carregamento do CSV (`online_retail_cleaned.csv`) como DataFrame com pandas.

### 🔹 2. Limpeza de dados  
- Remoção de valores ausentes nas colunas `CustomerID` e `Description`  
- Correção de quantidades negativas (interpretação e marcação como devolução)  
- Criação da coluna `Devolucao` (boolean) para identificar devoluções

### 🔹 3. Análise exploratória  
- Estatísticas descritivas das colunas numéricas  
- Comparação entre vendas e devoluções (análise percentual e gráfico de pizza)  
- Identificação dos principais países e produtos em termos de volume de vendas  
- Estudo da evolução mensal das vendas

### 🔹 4. Aplicação interativa (Streamlit)  
- Filtros por país, período e produto  
- Gráficos interativos usando Plotly  
- Interface limpa, intuitiva e responsiva  


---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**  
- **Pandas** – limpeza e manipulação de dados  
- **Streamlit** – aplicativo web interativo  
- **Plotly** – gráficos dinâmicos e visualmente ricos  

---


