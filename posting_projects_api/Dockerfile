FROM python:3.11


WORKDIR /app

RUN mkdir -p /app/data

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt


VOLUME /app/data

CMD ["python", "main.py"]