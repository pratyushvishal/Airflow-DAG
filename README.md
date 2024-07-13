# Airflow User Processing Pipeline

## Overview

This repository contains a data pipeline implemented using Apache Airflow. The pipeline is designed to extract user data from an API, process it, and store it in a PostgreSQL database. The project demonstrates the use of various Airflow operators and sensors, including the PostgresOperator, HttpSensor, SimpleHttpOperator, and PythonOperator.

## Features

- **Define a Data Pipeline**: The pipeline is defined using the Directed Acyclic Graph (DAG) in Airflow.
- **Execute SQL Requests**: Utilizes the PostgresOperator to create and interact with PostgreSQL tables.
- **Execute Python Functions**: Uses PythonOperator to process data and interact with files.
- **Execute HTTP Requests**: Leverages SimpleHttpOperator to extract data from an external API.
- **Wait for External Events**: Implements HttpSensor to wait for the API availability.
- **Access Secret Methods**: Uses Hooks, such as PostgresHook, to securely interact with databases.
- **Exchange Data Between Tasks**: Employs XCom to pass data between tasks within the DAG.

## Technologies Used

- **Apache Airflow**: For orchestrating and scheduling the data pipeline.
- **Docker**: For containerizing the Airflow environment.
- **PostgreSQL**: As the database for storing processed user data.
- **Python**: For data processing and interaction with Airflow.

## Getting Started

### Step 1: Clone the Repository


git clone https://github.com/pratyushvishal/Airflow-DAG.git


### Step 2: Set Up the Environment

docker-compose up -d


### Step 3: Access the Airflow Web UI
Open your web browser and navigate to http://localhost:8080 to access the Airflow web interface. Use the default credentials to log in:

Username: airflow
Password: airflow

### Step 4: Trigger the DAG
In the Airflow web interface, locate the user_processing DAG and trigger it manually or wait for the scheduled run.
