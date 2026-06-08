import pandas as pd
import os

def processar_vendas_gold():
    """Essa função le o arquivo salvo na pasta Silver, agrupa as vendas por categoria, gera os indicadores finmnceiros da camada Gold e salva o resultado em um novo arquivo parquet"""
    
    input_path = os.path.join('data', 'silver', 'vendas_v1_limpo.parquet')
    output_path = os.path.join('data', 'gold', 'vendas_v1_final.parquet')

    df = pd.read_parquet(input_path)

    df['valor'] = pd.to_numeric(df['valor'], errors ='coerce')
    df_gold = df.groupby('categoria').agg({'valor': 'sum','id_transacao':'count'}).reset_index().rename(columns={'valor': 'total_vendas_categoria','id_transacao':'quantidade_transacoes'})

    df_gold['ticket_medio'] = (df_gold['total_vendas_categoria'] / df_gold['quantidade_transacoes']).round(2)

    print(df_gold)
    
    df_gold.to_parquet(output_path, index=False)

    print("Processamento Gold concluído!",
          len(df_gold), "categorias processadas")

if __name__ == "__main__":
    processar_vendas_gold()

