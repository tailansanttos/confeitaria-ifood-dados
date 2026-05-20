import os

pasta_raw = "../data/raw"

for arquivo in os.listdir(pasta_raw):
    if arquivo.endswith(".xlsx.zip"):
        caminho_antigo = os.path.join(pasta_raw, arquivo)
        novo_nome = arquivo.replace('.xlsx.zip', '.xlsx')
        caminho_novo = os.path.join(pasta_raw, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f'Corrigido: {arquivo} -> {novo_nome}')
print("Todos arquivos foram corrigidos.")