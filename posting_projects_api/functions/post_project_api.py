import requests
from dotenv import load_dotenv
import pandas as pd
import os
from track_logs.logs import track_logs

load_dotenv(".env")

def post_projects(filename: str):
    
    df = pd.read_csv(filename)

    # get a valid apikey and the endpoint to make the 'POST' request
    API_KEY = os.getenv("PUBLIC_API_KEY")
    headers = {
        "Api-Key": API_KEY
    }

    # This is the server, this can change
    URL = "http://api_house_finder:8000/api/v1/add-project"

    for index, row in df.iterrows():
        # create a dictionary of parameters according to API Documentation
        parameters = {
            "name" : row["name"],
            "logo" : row["logo"],
            "location" : row["location"],
            "city" : row["city"],
            "company" : row["company"],
            "address" : row["address"],
            "contact" : row["contact"],
            "area" : row["area"],
            "price" : row["price"],
            "type" : row["type"],
            "img_url" : row["img_url"],
            "description" : row["description"],
            "url_website" : row["url_website"],
            "latitude" : row["latitude"],
            "longitude" : row["longitude"]
        }
        
        try:    
            # Sent the POST requests
            response = requests.post(url=URL, params=parameters, headers=headers)
            # watch the response
            track_logs(response.text)
        except Exception as ex:
            track_logs(ex)