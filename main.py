from src.ingestion.gerar_dados import gerar_vendas
from src.processing.processar_dados import carregar_e_salvar_bronze
from src.processing.limpeza_silver import processar_vendas_silver
from src.processing.processamento_gold import processar_vendas_gold

def executar_pipeline():
    print("🚀 Iniciando a pipeline de processamento de dados...")

    gerar_vendas()

    carregar_e_salvar_bronze()

    processar_vendas_silver()

    processar_vendas_gold()

    print("✅ Pipeline executada com sucesso!")

if __name__ == "__main__":
    executar_pipeline()
