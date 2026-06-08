import pandas as pd
import os
from src.security.encrypt import hash_dados_sensíveis

def processar_vendas_silver():

    input_path = os.path.join('data', 'bronze', 'vendas_v1.parquet')
    output_path = os.path.join('data', 'silver', 'vendas_v1_limpo.parquet')

    df = pd.read_parquet(input_path)

    schema_silver = {
        'id_transacao': 'str',
        'cliente_nome': 'str',
        'cliente_cpf': 'str',
        'produto' : 'str',
        'categoria': 'str',
        'valor': 'float'
    }
    df = df.astype(schema_silver)

    df['cliente_cpf'] = df['cliente_cpf'].apply(hash_dados_sensíveis)

    df['data_venda'] = pd.to_datetime(df['data_venda'], format='%Y-%m-%d', errors='coerce')

    print(df['data_venda'].isnull().sum())

    df['data_venda'] = pd.to_datetime(df['data_venda'].dt.date)

#    df['valor'] = df['valor'].round(2)

    df.to_parquet(output_path, index=False)
    print("Arquivo salvo com sucesso na camada Silver!")

if __name__ == "__main__":
    processar_vendas_silver()

