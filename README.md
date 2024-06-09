<div class="row ">
	<div class="col ">
		<h1  style="color:#C6AB7C; font-size: 80px; font-weight:bold;">WEB SCRAPING CONSTRUCTION COMPANIES</h1>
	</div>
</div>

<h4 align="justify">
      In the Atlantico department - Colombia, there are many housing projects, where people of all classes can get their own home, 
      but the information is not centered  in one company, each company has its information in own website, and to see webside by website is boring. 
</h4> 
<h4 align="justify">
      Knowing that, I investigated the main companies that are developing housing projects in Atlantico and start to scrap the data like name, type, 
	description, area of apartment and ect. After that, to store that information in a Excel file to watch the information to compare  project 
	by project like datasheet. 
</h4> 
<h4 align="justify">
     This project work together with the project <a href="https://github.com/kaacuna20/Website-house-project-searching-">"Website house project searching"</a>, to get that 
      information to enable fill the database with each data project.
</h4> 

This project is designed to scrape housing project data from various real estate company websites and process it into a structured format. The data is then saved into Excel files and used to make POST requests to an API. The entire process is Dockerized for easier setup and deployment.t.

## Table of Contents
- [Project Structure](#Project_Structure)
  - [Prerequisites](#Prerequisites)
  - [Environment Variables](#Environment_Variables)
  - [Building Docker Images](#Building_Docker_Images)
- [Running the Project](#Running_the_Project)
  - [Scraping Data](#Scraping_Data)
  - [Downloading Images](#Downloading_Images)
  - [Posting Data](#Posting_Data)
- [Details](#Details)
  - [Scraping Companies](#Scraping_Companies)
  - [Downloading Images](#Downloading_Images)
  - [Posting Data](#Posting_Data)
- [Docker Setup](#Docker_Setup)
  - [Main Dockerfile](#Main_Dockerfile)
  - [Running with Docker Compose](#Running_with_Docker_Compose)

## Project Structure
```ini
Website-house-project-searching/
├── companies_class/
│     ├── __init__.py
│     ├── amarilo_company.py
│     ├── arenas_inmobiliarias_company.py
│     ├── bolivar_company.py
│     ├── colpatria_company.py
│     ├── conaltura_company.py
│     ├── marval_company.py
│     ├── others_company.py
│     ├── prodesa_company.py
├── post_projects/
│     ├── Dockerfile
│     ├── post_project_api.py
│     ├── overwrite_projects.xlsx
│     ├── requirements.txt
│     ├── .env
│     ├── track_logs/
│          ├── logs.py
├── saved_data
│     ├── projects.xlsx
│     ├── log.log
│     └── static/images/img-projects
│			├── background
│                       └── logos
├── Dockerfile
├── .dockerignore
├── dataexcel.py
├── driver_selenium.py
├── main.py
├── requirements.txt
```
## Setup
### Prerequisites
Ensure you have Docker installed on your system. For local development, you also need Python 3.11 and pip.
### Environment Variables
Create a `.env` file in the post_projects/ directory with the following content:
```ini
PUBLIC_API_KEY=your_api_key_here
```
### Building Docker Images
1. Build the main scraping image:
```ini
docker build -t web-scraping .
```
2. Build the post request image:
```ini
cd post_projects
docker build -t post-projects .
cd ..
```
## Running the Project
### Scraping Data
1. Run the scraping container:
```ini
docker run --name web-scraping -v /path/to/local/saved_data:/app/saved_data web-scraping
```
This will scrape the data and save it to the saved_data/projects.xlsx file in your local directory.
### Downloading Images
1. Execute the Selenium script to download images:
```ini
python driver_selenium.py
```
### Posting Data
1. Run the POST request container:
```ini
docker run --name post-request --network housefinder_default -v /path/to/local/post_projects/logs:/app/logs post-projects
```
This will read the corrected Excel file post_projects/overwrite_projects.xlsx and send POST requests to the API.
## Details
### Scraping Companies
Each company has its own class in the `companies_class` directory, which handles the specifics of scraping data from their respective websites. Each class implements a method that returns a list of dictionaries, each dictionary containing data for a housing project.

### Saving Data
The `dataexcel.py` script gathers the data from all the company classes and writes it to an Excel file, saved_data/projects.xlsx.

### Downloading Images
The `driver_selenium.py` script uses Selenium to download images associated with each project (e.g., logos and background images) and saves them in the saved_data/static/images/img-projects directory.

### Posting Data
The `post_project_api.py` script reads data from the `post_projects/overwrite_projects.xlsx` file and sends it as POST requests to the specified API endpoint.

## Docker Setup
### Main Dockerfile
This Dockerfile sets up the environment for scraping and saving data.
```ini
FROM python:3.11

WORKDIR /app

RUN mkdir -p /app/saved_data

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

VOLUME /app/saved_data

CMD ["python", "main.py"]
```
### Post Projects Dockerfile
This Dockerfile sets up the environment for reading the Excel file and sending POST requests.
```ini
FROM python:3.11

WORKDIR /app

RUN mkdir -p /app/logs

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

VOLUME /app/logs

CMD ["python", "post_project_api.py"]
```
### Running with Docker Compose
If you are using Docker Compose, make sure your containers are connected to the appropriate network (`housefinder_default` in this case).
