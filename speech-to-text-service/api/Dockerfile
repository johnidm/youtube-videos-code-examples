FROM python:3.12.8-alpine3.21

WORKDIR /app

COPY api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .

EXPOSE 8000

CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]