import pandas as pd

def vendas_mensais():
    df = pd.read_csv('online_retail_cleaned.csv')

    # Converter InvoiceDate para datetime (por segurança, caso esteja como string)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Criar coluna com ano e mês
    df['AnoMes'] = df['InvoiceDate'].dt.to_period('M')

    # Considerar apenas vendas (quantidade positiva)
    df_vendas = df[~df['Devolucao']]

    # Agrupar por mês e somar quantidade vendida
    vendas_por_mes = df_vendas.groupby('AnoMes')['Quantity'].sum()

    print('\nVendas mensais (quantidade total de itens vendidos):')
    print(vendas_por_mes)

if __name__ == '__main__':
    vendas_mensais()
