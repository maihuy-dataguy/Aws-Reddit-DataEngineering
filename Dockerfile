FROM apache/airflow:latest-python3.12

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
ENTRYPOINT ["gunicorn","--workers", "1", "--timeout", "1000", "--bind", "0.0.0.0:8000", "wsgi:app"]
