import pandas as pd
from pathlib import Path

path_relatorio = Path(__file__).parent.parent / "data"/"raw"/"relatorios.csv"
coluna_status = ["STATUS FINAL DO PEDIDO"]

def create_dataframe(path_name: str) -> pd.DataFrame:
    print(f'Criando Dataframe.')
    path = Path(path_name)

    if not path.exists:
        print(f'Arquivo {path} não encontrado.')
        return pd.DataFrame

    df = pd.read_csv(path)
    print(f'Dataframe criado com {len(df)} linhas.')
    return df



def remove_nulos(df:pd.DataFrame) -> pd.DataFrame:

    df = df.dropna()
    return df
def padronizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("(r$)", "").str.strip("_")
    return df


def padronizar_datetime(df: pd.DataFrame) -> pd.DataFrame:
    df["data_e_hora_do_pedido"] = pd.to_datetime(df['data_e_hora_do_pedido'], dayfirst=True)
    df["data_pedido"] = df["data_e_hora_do_pedido"].dt.date
    df["hora_pedido"] = df['data_e_hora_do_pedido'].dt.time
    return df 

def salvar_df_processado(df: pd.DataFrame):
    path = Path(__file__).parent.parent / "data" / "processed" / "relatorio_pedidos.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path)



def transformation_data() -> pd.DataFrame:
    print(f'Iniciando transformação dos dados.')
    df = create_dataframe(path_relatorio)
    print(f"Arquivo com {len(df)} valores antes da transformação.")
    df = remove_nulos(df)
    df = padronizar_colunas(df)
    df = padronizar_datetime(df)
    salvar_df_processado(df)
    print(f"Transformação concluida com sucesso. Relatório com {len(df)} valores pós transformação.")

transformation_data()