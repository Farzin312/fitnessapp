FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV NAME World

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
