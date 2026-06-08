import subprocess

def run_step(command):
    print(f"Executando: {command}...")
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    run_step("python src/ingestion/gerar_dados.py")
    run_step("python -m src.processing.processar_dados")
    run_step("python -m src.processing.limpeza_silver")
    run_step("python -m src.processing.processamento_gold")
    print("🚀 Pipeline completo executado com sucesso!")