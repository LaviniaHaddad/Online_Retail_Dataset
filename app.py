import streamlit as st
import pandas as pd
import plotly.express as px

# Função para carregar dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("online_retail_cleaned.csv")
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['AnoMes'] = df['InvoiceDate'].dt.to_period('M')
    return df

df = carregar_dados()

# Sidebar - Título e filtros
st.sidebar.title("🛍️ Análise de Vendas - Online Retail")

# Filtro por país
paises = sorted(df['Country'].dropna().unique())
pais_selecionado = st.sidebar.multiselect("🌍 Selecione o(s) país(es):", paises, default=["United Kingdom"])

# Filtro por produto
produtos = sorted(df['Description'].dropna().unique())
produto_selecionado = st.sidebar.multiselect("📦 Filtrar por produto (opcional):", produtos, default=[])

# Filtro por data
min_data = df['InvoiceDate'].min().date()
max_data = df['InvoiceDate'].max().date()
data_inicial, data_final = st.sidebar.date_input("🗓️ Período de vendas:", [min_data, max_data],
                                                 min_value=min_data, max_value=max_data)

# Aplica os filtros ao DataFrame
df_filtrado = df[
    (df['Country'].isin(pais_selecionado)) &
    (df['InvoiceDate'].dt.date >= data_inicial) &
    (df['InvoiceDate'].dt.date <= data_final)
]

if produto_selecionado:
    df_filtrado = df_filtrado[df_filtrado['Description'].isin(produto_selecionado)]

# Navegação principal
pagina = st.sidebar.radio("📂 Página:", [
    "Resumo Estatístico",
    "Vendas x Devoluções",
    "Top Países",
    "Top Produtos",
    "Vendas Mensais"
])

# Página: Resumo Estatístico
if pagina == "Resumo Estatístico":
    st.title("📊 Resumo Estatístico")
    st.write(df_filtrado.describe())

# Página: Vendas x Devoluções
elif pagina == "Vendas x Devoluções":
    st.title("📦 Vendas x Devoluções")
    total_vendido = df_filtrado.loc[~df_filtrado['Devolucao'], 'Quantity'].sum()
    total_devolvido = df_filtrado.loc[df_filtrado['Devolucao'], 'Quantity'].sum()
    percentual = round(abs(total_devolvido) / total_vendido * 100, 2) if total_vendido != 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Vendido", int(total_vendido))
    col2.metric("Total Devolvido", int(total_devolvido))
    col3.metric("Percentual Devolvido", f"{percentual}%")

    df_tmp = df_filtrado.groupby('Devolucao')['Quantity'].sum().reset_index()
    df_tmp['Tipo'] = df_tmp['Devolucao'].map({True: "Devolução", False: "Venda"})

    fig = px.pie(df_tmp, values='Quantity', names='Tipo',
                 title="Distribuição de Vendas e Devoluções",
                 color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig)

# Página: Top Países
elif pagina == "Top Países":
    st.title("🌍 Top Países por Vendas")
    vendas = df_filtrado[~df_filtrado['Devolucao']].groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
    fig = px.bar(vendas, x=vendas.index, y=vendas.values,
                 labels={'x': 'País', 'y': 'Quantidade Vendida'},
                 title="Top 10 Países por Quantidade Vendida")
    st.plotly_chart(fig)

# Página: Top Produtos
elif pagina == "Top Produtos":
    st.title("🏆 Top Produtos Mais Vendidos")
    top_prod = df_filtrado[~df_filtrado['Devolucao']].groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    fig = px.bar(top_prod, x=top_prod.values, y=top_prod.index,
                 orientation='h',
                 labels={'x': 'Quantidade Vendida', 'y': 'Produto'},
                 title="Top 10 Produtos por Quantidade Vendida")
    st.plotly_chart(fig)

# Página: Vendas Mensais
elif pagina == "Vendas Mensais":
    st.title("📅 Evolução Mensal de Vendas")
    vendas_mes = df_filtrado[~df_filtrado['Devolucao']].groupby('AnoMes')['Quantity'].sum()
    vendas_mes.index = vendas_mes.index.astype(str)
    fig = px.line(x=vendas_mes.index, y=vendas_mes.values,
                  labels={'x': 'Ano-Mês', 'y': 'Quantidade Vendida'},
                  title="Vendas Mensais")
    st.plotly_chart(fig)