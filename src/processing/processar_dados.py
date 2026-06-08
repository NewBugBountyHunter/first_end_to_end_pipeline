import pandas as pd
import json
import os


input_path = os.path.join('data', 'raw', 'vendas_brutas.json')
output_path = os.path.join('data', 'bronze', 'vendas_v1.parquet')

def carregar_e_inspecionar():

    df = pd.read_json(input_path)
    print("---Primeiras 5 linhas---")
    print(df.head(5))
    print("\n--- Informações dos Dados ---")
    print(df.info())

def carregar_e_salvar_bronze():
    df = pd.read_json(input_path)
    df['origem_arquivo'] = input_path
    df.to_parquet(output_path, index=False)
    print(f"Sucesso! Dado arquivado em Bronze: {output_path}")



if __name__ == "__main__":
    carregar_e_inspecionar()
    carregar_e_salvar_bronze()