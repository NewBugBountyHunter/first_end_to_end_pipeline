import json
import os
import random
from datetime import datetime

# Criando a pasta raw se não existir
os.makedirs('data/raw', exist_ok=True)

produtos = [
    {"nome": "Smartphone G5", "categoria": "Eletrônicos", "preco": 2500.00},
    {"nome": "Notebook Pro", "categoria": "Informática", "preco": 5500.00},
    {"nome": "Cadeira Gamer", "categoria": "Móveis", "preco": 1200.00},
    {"nome": "Fone Bluetooth", "categoria": "Acessórios", "preco": 300.00}
]

nomes = ["João Silva", "Maria Oliveira", "Carlos Souza", "Ana Costa", "Bruno Alves"]

def gerar_vendas(n=100):
    vendas = []
    for i in range(n):
        prod = random.choice(produtos)
        venda = {
            "id_transacao": f"TRX-{random.randint(1000, 9999)}",
            "cliente_nome": random.choice(nomes),
            "cliente_cpf": f"{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}",
            "produto": prod["nome"],
            "categoria": prod["categoria"],
            "valor": prod["preco"] * random.uniform(0.8, 1.2), # Simula descontos
            "data_venda": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        vendas.append(venda)
    
    with open('data/raw/vendas_brutas.json', 'w') as f:
        json.dump(vendas, f, indent=4)
    print(f"Sucesso! 100 vendas geradas em 'data/raw/vendas_brutas.json'")

if __name__ == "__main__":
    gerar_vendas()