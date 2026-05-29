from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import os
from sqlalchemy import create_engine, text

# Lendo o .env diretamente da RAIZ do projeto no Docker
env_path = Path("/opt/airflow/.env")

if env_path.exists() and env_path.is_file():
    load_dotenv(env_path)
else:
    print("ALERTA: Arquivo .env não encontrado na raiz!")

user = os.getenv('DB_USER')
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT", "5432")

def criar_conexao_banco():
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

engine = criar_conexao_banco()

def criar_tabela(df: pd.DataFrame):
    # Força a exclusão em cascata antes de recriar para não conflitar com as views
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS pedidos_fatos CASCADE;"))
        
    df.to_sql("pedidos_fatos", engine, if_exists="replace", index=False)
    print(f'Tabela criada no banco')

def inserir_dados_tabela(arquivos: list):
    for arquivo in arquivos:
        df = pd.read_csv(arquivo)
        criar_tabela(df)
    print(f'Carregamento dos dados realizados na tabela.')

def database_main():
    pasta = Path('/opt/airflow/data/processed')
    if not pasta.exists():
        print(f'Pasta não encontrada.')
        return
    if not pasta.is_dir():
        print(f'Caminho não é uma pasta.')
        return
    arquivos = list(pasta.glob('*.csv'))
    inserir_dados_tabela(arquivos)

if __name__== '__main__':
    database_main()