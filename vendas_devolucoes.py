import pandas as pd

def analisar_vendas_devolucoes():
    df = pd.read_csv('online_retail_cleaned.csv')

    # Vendas: linhas onde a quantidade é positiva
    total_vendido = df.loc[~df['Devolucao'], 'Quantity'].sum()

    # Devoluções: linhas onde a quantidade é negativa
    total_devolvido = df.loc[df['Devolucao'], 'Quantity'].sum()

    print(f'Total de itens vendidos: {total_vendido}')
    print(f'Total de itens devolvidos: {total_devolvido}')
    print(f'Percentual de devoluções: {round(abs(total_devolvido) / total_vendido * 100, 2)}%')

if __name__ == '__main__':
    analisar_vendas_devolucoes()
