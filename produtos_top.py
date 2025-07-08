import pandas as pd

def produtos_mais_vendidos():
    df = pd.read_csv('online_retail_cleaned.csv')

    # Considerar apenas vendas (quantidade positiva)
    df_vendas = df[~df['Devolucao']]

    # Agrupar por descrição do produto e somar as quantidades
    top_produtos = df_vendas.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

    print('\nTop 10 produtos mais vendidos (por quantidade):')
    print(top_produtos)

if __name__ == '__main__':
    produtos_mais_vendidos()