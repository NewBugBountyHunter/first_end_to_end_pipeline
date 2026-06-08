import hashlib

def hash_dados_sensíveis(dados):
    dado_string = dados.strip()
    dados_bytes = dado_string.encode('utf-8')
    return hashlib.sha256(dados_bytes).hexdigest()