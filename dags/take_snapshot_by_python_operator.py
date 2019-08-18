import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import time
import requests
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    "start_date": airflow.utils.dates.days_ago(1),
    }



dag = DAG('click_stream', default_args=default_args, schedule_interval='0 11 * * *')


run_python_file = """
    cd `pwd` ; 
"""

def slack_notification():
    pass

t1 = BashOperator(
    task_id = 'top_keywords',
    bash_command = run_python_file,
    params = {"file_name":"top_keywords.py"},
    dag = dag,)

t2 = BashOperator(
    task_id = 'top_pages',
    bash_command = run_python_file,
    params = {"file_name":"top_pages.py"},
    dag = dag,
    )

t3 = PythonOperator(
        task_id = 'send_slack_notification',
        python_callable = slack_notification,
        # op_kwargs={'random_base': float(i)/10},
        dag=dag)


t2.set_upstream(t1)
t3.set_upstream(t2)

