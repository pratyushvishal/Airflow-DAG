from airflow import DAG

from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
import json

with DAG('user_processing', start_date = datetime(2024,7,11),
            schedule_interval='@daily', catchup=False) as dag: 
    
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id = 'postgres',
        sql='''
            create table if not exists users(
            firstname text not null,
            lastname text not null,
            country text not null,
            username text not null,
            password text not null,
            email text not null
            );
        '''
    )


    is_api_available = HttpSensor(
        task_id= 'is_api_available',
        http_conn_id = 'user_api',
        endpoint="api/"
    )

    extract_user = SimpleHttpOperator(
        task_id = 'extract_user',
        http_conn_id = 'api/',
        method = 'GET',
        response_filter = lambda response:json.loads(response.text),
        log_response = True
    )



