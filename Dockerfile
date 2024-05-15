FROM python:3.8-slim
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements_torch.txt /app/
# Intentar instalar torch con un bucle de reintento
RUN set -e; \
    for i in 1 2 3 4 5; do \
        echo "Attempt $i: Installing torch..."; \
        pip install --no-cache-dir --default-timeout=1200 -r requirements_torch.txt && break || \
        echo "Attempt $i failed. Retrying in 30 seconds..." && sleep 30; \
    done; \
    if [ $i -eq 5 ]; then \
        echo "Final attempt failed. Exiting."; \
        exit 1; \
    fi

# Copiar e instalar otras dependencias
COPY requirements_rest.txt /app/
RUN set -e; \
    for i in 1 2 3 4 5; do \
        echo "Attempt $i: Installing other dependencies..."; \
        pip install --no-cache-dir --default-timeout=1200 -r requirements_rest.txt && break || \
        echo "Attempt $i failed. Retrying in 30 seconds..."; \
        sleep 30; \
    done; \
    if [ $i -eq 5 ]; then \
        echo "Final attempt failed. Exiting."; \
        exit 1; \
    fi

COPY . /app/

RUN chmod +x /app/gunicorn_starter.sh

EXPOSE 8003

CMD ["/app/gunicorn_starter.sh"]
