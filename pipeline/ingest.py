import pandas as pd
import os
from pathlib import Path
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module="openpyxl")

pasta_raw = "/opt/airflow/data/raw"

def ingestao_dados() -> pd.DataFrame:
    arquivos_excel = [f for f in os.listdir(pasta_raw) if f.endswith(".xlsx") and not f.startswith("~$")]
    lista_dataframes = []

    print("Iniciando leitura dos arquivos.")
    for arquivo in arquivos_excel:
        caminho_completo = os.path.join(pasta_raw, arquivo)

        try:
            df_temporario = pd.read_excel(caminho_completo)
            df_temporario['arquivo_origem'] = arquivo
            lista_dataframes.append(df_temporario)
            print(f'Arquivo lido com sucesso: {arquivo}')
        except Exception as e:
            print(f'Arquivo descartado: {arquivo}. Motivo: Formato inválido.')
    
    if not lista_dataframes:
        print("Nenhum arquivo válido foi encontrado.")
        return None
    
    df_consolidado = pd.concat(lista_dataframes, ignore_index=True)

    output_path = Path("/opt/airflow/data/raw/relatorios.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_consolidado.to_csv(output_path, index=False)

    print("-" * 30)
    print(f'Arquivos consolidados.')
    print(f'Arquivo salvo em {output_path}')
    return df_consolidado

if __name__ == '__main__':
    ingestao_dados()