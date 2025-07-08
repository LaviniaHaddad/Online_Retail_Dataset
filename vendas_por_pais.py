import pandas as pd

def vendas_por_pais():
    df = pd.read_csv('online_retail_cleaned.csv')

    # Considerar apenas vendas (quantidade positiva)
    df_vendas = df[~df['Devolucao']]

    # Agrupar por país e somar quantidade
    vendas = df_vendas.groupby('Country')['Quantity'].sum().sort_values(ascending=False)

    print('\nTop 10 países com maior quantidade vendida:')
    print(vendas.head(10))

    print('\nNúmero total de países com vendas registradas:', vendas.shape[0])

if __name__ == '__main__':
    vendas_por_pais()
