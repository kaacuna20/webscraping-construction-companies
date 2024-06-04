FROM python:3.11


WORKDIR /app

RUN mkdir -p /app/saved_data



COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt


# Download and install ChromeDriver docker run --name web-scraping -v C:/Users/57300/Documents/MY PYTHON-KEVIN/my portfolio/web_scraping_database/saved_data:/app/saved_data web-scraping
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean


VOLUME /app/saved_data


CMD ["python", "main.py"]