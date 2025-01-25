# Aws-Reddit-DataEngineering

## Introduction
This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## System Architecture
![System Architecture](https://github.com/maihuy-dataguy/Aws-Reddit-DataEngineering/blob/main/pics/RedditDataEngineering.png)


The project is designed with the following Technology Stack:

- **Reddit API** : Used for extracting data by subreddit, limit 100 records.
- **Apache Airflow**: Used for scheduling the data lineage, extracting data from Reddit throguh Reddit API and push data into S3 Buckekt. Airflow includes some important components:
    - Scheduler: handles both triggering scheduled workflows, and submitting Tasks to the workers to run.
    - Workers: executes the tasks given to it by the scheduler. 
    - PostgreSql: A metadata database, which airflow components use to store state of workflows and tasks.
    - Celery: the Celery executor will be used in this project.Airflow tasks are sent to a central queue (Reddit) where remote workers pull tasks to execute.
    - Webserver: which presents a handy user interface to inspect, trigger and debug the behaviour of DAGs and tasks.
- **Docker**: For deploying containers running Apache Airflow components.
- **Simple Storage Service (S3)**: destination storage from airflow, object storage service can be regarded as a data lake
- **AWS Glue**: Manage ETL jobs, we are going to transform data through Spark and load back into S3. Create metadata tables definition stored in data catalog by running crawlers. 
- **AWS Athena**: For querying the transformed data beneath S3. Querying through database and metadata tables created from AWS Glue crawlers
- **Amazon Redshift**: For data warehousing, we can query and make statistics from external table created from external database AWS Glue Data Catalog.
- **BI Tools**: we can connect to tableau, looker, power bi through Redshift endpoint, AWS Athena or Data catalog connection.

## Prerequisites
- AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials. Check [here](https://www.reddit.com/r/reddit.com/wiki/api/) for more information
- Docker Installation
- Python 3.12 (to this point)
