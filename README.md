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
- [Project Structure](#Project-Structure)
  - [Prerequisites](#Prerequisites)
  - [Environment Variables](#Environment-Variables)
  - [Building Docker Images](#Building-Docker-Images)
- [Running the Project](#Running-the-Project)
  - [Scraping Data](#Scraping-Data)
  - [Downloading Images](#Downloading-Images)
  - [Posting Data](#Posting-Data)
- [Details](#Details)
  - [Scraping Companies](#Scraping-Companies)
  - [Downloading Images](#Downloading-Images)
  - [Posting Data](#Posting-Data)
- [Docker Setup](#Docker-Setup)
  - [Main Dockerfile](#Main-Dockerfile)


## Project Structure
```ini
Website-house-project-searching/
├── web_scrpaing_companies
|   ├── dataexcel.py
|   ├── Dockerfile
|   ├── requirements.txt
|   ├── track_logs/
|   |    └── logs.py
|   ├── saved_documents/
|   |    ├── projects.xlsx
|   |    └── log.log
|   └── companies_class/
|       ├── __init__.py
|       ├── amarilo_company.py
|       ├── arenas_inmobiliarias_company.py
|       ├── bolivar_company.py
|       ├── colpatria_company.py
|       ├── conaltura_company.py
|       ├── marval_company.py
|       ├── others_company.py
|       └── prodesa_company.py
|
└── posting_projects_api/
   ├── .env
   ├── main.py
   ├── Dockerfile
   ├── requirements.txt
   ├── overwrite_projects.xlsx
   ├── track_logs/
   |    └── logs.py
   └── data/
   |    ├── log.log
   |    └── projects.csv
   └── functions/
       ├── __init__.py
       ├── add_coordinates.py
       ├── convert_to_csv.py
       ├── bolivar_company.py
       ├── google_maps_api.py
       └── post_project_api.py



```
## Setup
### Prerequisites
Ensure you have Docker installed on your system. For local development, you also need Python 3.11 and pip.
### Environment Variables
Create a `.env` file in the posting_projects_api/ directory with the following content:
```ini
PUBLIC_API_KEY=your_api_key_here
```
### Building Docker Images
1. Build the main scraping image:
```ini
cd web_scraping_companies
docker build -t web-scraping-companies .

```
2. Build the post request image:
```ini
cd post_projects
docker build -t posting-projects .
```
## Running the Project
### Scraping Data
1. Run the scraping container:
```ini
docker run --name web-scraping -v /path/to/local/saved_documents:/app/saved_documents web-scraping-companies
```
This will scrape the data and save it to the saved_data/projects.xlsx file in your local directory.

### Posting Data
1. Run the POST request container:
```ini
docker run --name posting-projects --network house_finder_web -v /path/to/local/data:/app/data posting-projects
```
This will read the corrected Excel file to convert a file.csv and with that file, send POST requests to the API.
## Details
### Scraping Companies
Each company has its own class in the `companies_class` directory, which handles the specifics of scraping data from their respective websites. Each class implements a method that returns a list of dictionaries, each dictionary containing data for a housing project.

### Saving Data
The `dataexcel.py` script gathers the data from all the company classes and writes it to an Excel file, saved_data/projects.xlsx.

### Posting Data
The `main.py` script reads data from the `overwrite_projects.xlsx` file, first, using the google maps api, get the coordinates of each project writing the name, city of each project and concatenate with `Atlántico`, later, adding those coordinates to each project and later saving this in file.csv, this beacuse at moment to send psot request, this is easier to read and sends it as POST requests to the specified API endpoint.

## Docker Setup
### Web_scraping_companies Dockerfile
This Dockerfile sets up the environment for scraping and saving data.
```ini
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
```
### Posting_projects_api Dockerfile
This Dockerfile sets up the environment for reading the Excel file and sending POST requests.
```ini
FROM python:3.11

WORKDIR /app

RUN mkdir -p /app/data

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

VOLUME /app/data

CMD ["python", "main.py"]
```

