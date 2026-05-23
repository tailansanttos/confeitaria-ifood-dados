import psycopg2
from pathlib import Path
from dotenv import load_dotenv
import os

dir_base = Path(__file__).resolve().parent.parent
load_dotenv(dir_base /".env")
pasta_sql = dir_base / "queries"


def conectar_banco():
    try:
        print(f'Tentando conexão com o banco.')
        conexao = psycopg2.connect(dbname =os.getenv("DB_DATABASE"), user=os.getenv("DB_USER"),
                                   password= os.getenv("DB_PASSWORD"), host= os.getenv("DB_HOST"),
                                    port=os.getenv("DB_PORT") )
        cursor = conexao.cursor()
        
        arquivos_sql = sorted(pasta_sql.glob("*.sql"))
        if not arquivos_sql:
            print("NEnhum arquivo SQL encontrado.")
        
        for caminho_arquivo in arquivos_sql:
            nome_arquivo = caminho_arquivo.name
            print(f'Executando {nome_arquivo}')

            query = caminho_arquivo.read_text(encoding='utf-8')
            cursor.execute(query)
            
        conexao.commit()
        print(f'Sucesso. {len(arquivos_sql)} views foram criadas/atualizadas.')
    except Exception as e:
        print(f"Erro. A execução falhou. Detalhe {e}")
        if 'conexao' in locals():
            conexao.rollback()
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

conectar_banco()