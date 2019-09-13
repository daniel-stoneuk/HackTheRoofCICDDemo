FROM python:3.7-alpine

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

CMD ["gunicorn","--config", "./gunicorn_app/conf/gunicorn_config.py", "my_app:app"]
