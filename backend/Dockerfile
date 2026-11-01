FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y && apt-get install -y nano \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Manila
WORKDIR /app

COPY  requirements.txt ./

RUN pip install -r requirements.txt


COPY . .

CMD ["gunicorn", "main:app","-k", "uvicorn.workers.UvicornWorker","-w","4", "--bind", "0.0.0.0:8006", "--timeout", "3000", "--graceful-timeout", "3000"]

EXPOSE 8006

