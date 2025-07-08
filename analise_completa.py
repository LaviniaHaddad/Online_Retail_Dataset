import pandas as pd

def carregar_dados():
    df = pd.read_csv('online_retail_cleaned.csv')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['AnoMes'] = df['InvoiceDate'].dt.to_period('M')
    return df

def resumo_estatistico(df):
    print('📊 RESUMO ESTATÍSTICO:')
    print(df.describe())
    print('\n' + '='*80 + '\n')

def vendas_devolucoes(df):
    total_vendido = df.loc[~df['Devolucao'], 'Quantity'].sum()
    total_devolvido = df.loc[df['Devolucao'], 'Quantity'].sum()
    print('📦 VENDAS E DEVOLUÇÕES:')
    print(f'Total vendido: {total_vendido}')
    print(f'Total devolvido: {total_devolvido}')
    print(f'Percentual de devolução: {round(abs(total_devolvido) / total_vendido * 100, 2)}%')
    print('\n' + '='*80 + '\n')

def vendas_por_pais(df):
    vendas = df[~df['Devolucao']].groupby('Country')['Quantity'].sum().sort_values(ascending=False)
    print('🌍 TOP 10 PAÍSES POR QUANTIDADE VENDIDA:')
    print(vendas.head(10))
    print(f'\nTotal de países com vendas registradas: {vendas.shape[0]}')
    print('\n' + '='*80 + '\n')

def vendas_mensais(df):
    vendas_mes = df[~df['Devolucao']].groupby('AnoMes')['Quantity'].sum()
    print('📅 VENDAS MENSAIS:')
    print(vendas_mes)
    print('\n' + '='*80 + '\n')

def produtos_top(df):
    top_prod = df[~df['Devolucao']].groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    print('🏆 TOP 10 PRODUTOS MAIS VENDIDOS:')
    print(top_prod)
    print('\n' + '='*80 + '\n')

if __name__ == '__main__':
    df = carregar_dados()
    resumo_estatistico(df)
    vendas_devolucoes(df)
    vendas_por_pais(df)
    vendas_mensais(df)
    produtos_top(df)