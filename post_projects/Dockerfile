FROM python:3.11


WORKDIR /app

RUN mkdir -p /app/logs

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt


VOLUME /app/logs
#docker run --name post-request --network housefinder_default -v C:/Users/57300/Documents/docker/scrap/web_scraping_database/post_projects/logs:/app/logs post-projects

CMD ["python", "post_project_api.py"]