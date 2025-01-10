FROM python:3.12.8-slim-bookworm

WORKDIR /app

COPY worker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY worker/ .

ENV CELERY_BROKER_URL=redis://redis:6379/0
ENV CELERY_RESULT_BACKEND=redis://redis:6379/0

CMD ["celery", "-A", "main.celery_app", "worker", "--loglevel=info"]
