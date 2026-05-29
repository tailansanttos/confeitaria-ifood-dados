from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG
from pathlib import Path
from pipeline.limpa_nomes import arrumar_arquivos
from pipeline.ingest import ingestao_dados
from pipeline.transform import transformation_data
from pipeline.load import database_main
from pipeline.create_views import criar_views

default_args  = {
    'owner':'Tailan',
    'retries':2,
    'retry_delay': timedelta(minutes=5),
    'email_in_future':False
}

with DAG(
    dag_id="dag_pipeline_dados_ifood", 
    default_args= default_args,
    schedule="@daily", 
      start_date=datetime(2026, 5, 28),
      description="Airflow Pipeline de dados ifood.", tags=['airflow', 'python', 'dados_ifood']
) as dag:

      tarefa_arrumar_arquivos   = PythonOperator(
        task_id='arrumar_arquivos',
        python_callable=arrumar_arquivos
        )
      
      tarefa_ingestao_dados = PythonOperator(
        task_id= 'ingestao_dados',
        python_callable=ingestao_dados
      )

      tarefa_transformar_dados = PythonOperator(
          task_id= 'transformacao_dados',
          python_callable= transformation_data
      )

      tarefa_carregar_dados_banco = PythonOperator(
           task_id= 'carregar_dados_banco',
           python_callable= database_main
      )

      tarefa_criar_views = PythonOperator(
           task_id='criar_views',
           python_callable=criar_views
      )

      (tarefa_arrumar_arquivos >> tarefa_ingestao_dados >> tarefa_transformar_dados >> tarefa_carregar_dados_banco >> tarefa_criar_views)

