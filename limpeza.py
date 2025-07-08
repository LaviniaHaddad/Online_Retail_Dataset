import pandas as pd

def limpar_dados():
    caminho = r'C:\Users\Cliente\Desktop\Python\Online Retail Dataset\data.csv'

    df = pd.read_csv(caminho, encoding='latin1')

    # Converter InvoiceDate para datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Remover duplicatas
    df = df.drop_duplicates()

    # Remover linhas sem CustomerID
    df = df.dropna(subset=['CustomerID'])

    # Preencher descrições faltantes
    df['Description'] = df['Description'].fillna('Unknown')

    # Criar coluna para marcar devoluções
    df['Devolucao'] = df['Quantity'] < 0

    # Remover preços zero ou negativos
    df = df[df['UnitPrice'] > 0]

    # Salvar arquivo limpo
    df.to_csv('online_retail_cleaned.csv', index=False)
    print(f'Dados limpos salvos em online_retail_cleaned.csv. Tamanho final: {df.shape}')

if __name__ == '__main__':
    limpar_dados()