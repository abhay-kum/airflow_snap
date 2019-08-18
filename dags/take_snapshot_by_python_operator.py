import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import time
import requests
import json

# default args for dags configuration
# you can refer to documentation
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    "start_date": airflow.utils.dates.days_ago(1),
    }


dag = DAG('snapshot_for_daily', default_args=default_args, schedule_interval='0 11 * * *')

# using jinja template

run_python_file = """
    cd  `pwd`;
    python snapshot/{{params.file_name}};
"""

task1 = BashOperator(
    task_id = 'take_snap_by_splinter',
    bash_command = run_python_file,
    params = {"file_name":"take_snapshot.py"},
    dag = dag,)

task2 = BashOperator(
    task_id = 'send_to_google_drive',
    bash_command = run_python_file,
    params = {"file_name":"top_pages.py"},
    dag = dag,
    )

task3 = PythonOperator(
        task_id = 'delete_image',
        python_callable = delete_file,
        # op_kwargs={'random_base': float(i)/10},
        dag=dag)

task2.set_upstream(task1)
task3.set_upstream(task2)
