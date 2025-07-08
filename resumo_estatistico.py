import pandas as pd

def resumo_estatistico():
    df = pd.read_csv('online_retail_cleaned.csv')

    print('Resumo estatístico das colunas numéricas:')
    print(df.describe())

if __name__ == '__main__':
    resumo_estatistico()