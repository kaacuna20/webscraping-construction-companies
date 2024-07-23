from bs4 import BeautifulSoup
import requests
from track_logs.logs import track_logs

# lists of endpoints
list_endpoint = [
    "senza",
    "bavaro",
    "catara"
]

class ConalturaProject:

    def __init__(self):
        self.main_endpoint = "https://conaltura.com/proyectos-de-vivienda-nueva/"
        self.all_projects_by_catara = []

    def get_projects(self) -> list:
        index = 0
        for project in list_endpoint:
            # Get the url to start scraping
            response = requests.get(f"{self.main_endpoint}{project}")
            track_logs(f"{self.main_endpoint}{project}")

            soup = BeautifulSoup(response.text, "html.parser")
            # get url of website
            url_website = f"{self.main_endpoint}{project}"
            # get the name of project
            name = soup.title.text.split(" - ")[0].title()
            # get the src of logo
            logo = soup.find(name="div", class_="contenedor logo center text-center logo").select_one("img").get("src")
            # get the location of project
            location = soup.find(name="h4", class_="text-white font-weight-bold").text.title()
            # get the price of project in COP
            price = soup.find(name="h2", class_="fz-100 font-weight-bold").text.split("$")[1].replace(".", "").replace("'", "")
            # get the area in m2 of apartment
            area = soup.find(name="h5", class_="text-conaltura-dark font-weight-bold descripciondetalle").text.split("m")[0].strip()
            # get a summary about the project
            description = soup.find(name="p", class_="text-conaltura-dark text-justify descripcion mb-5").text.replace("Ã¡", "a").replace("Ã³", "a").replace("Ãº", "u")
            # get the contact to ask information
            contact = soup.find_all(name="li", class_="liSalaventas m-2")[4].text.split(":")[1]
            # get the address of salesroom
            address = soup.find_all(name="li", class_="liSalaventas m-2")[2].text.split(":")[1]
            # All projects are type 'VIS'
            type = "VIS"
            # get the city
            city = soup.find_all(name="li", class_="liSalaventas m-2")[3].text.split(":")[1].strip()
            # get the src of background of project
            url_img = soup.find(name="div", class_="carousel-item active").select_one("img").get("src")

            # make the dictionary with each item scraped
            dict_by_project = {
                "name": name,
                "logo": logo,
                "location": location,
                "city": city,
                "company": "Conaltura",
                "address": address,
                "contact": contact,
                "area": area,
                "price": price,
                "type": type,
                "img_url": url_img,
                "description": description,
                "url_website": url_website
            }
            self.all_projects_by_catara.append(dict_by_project)
            index += 1
        return self.all_projects_by_catara


