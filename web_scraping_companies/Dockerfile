FROM python:3.11


WORKDIR /app

RUN mkdir -p /app/saved_documents



COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

VOLUME /app/saved_documents


CMD ["python", "dataexcel.py"]