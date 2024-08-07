from bs4 import BeautifulSoup
import requests
from track_logs.logs import track_logs

# list that content the endpoints, types, city and location of each project
list_endpoint = [
    # [endpoint, type, city, location]
    ["proyecto-almeria/", "VIS", "Barranquilla", "Andalucía"],
    ["ibaia-apartamentos/", "NO VIS", "Barranquilla", "Ciudad Jardín"],
    ["acuarela-del-rio/", "NO VIS", "Barranquilla", "Malecón del río"],
    ["guayacanes-apartamentos/", "VIS", "Soledad", "P.R. Nuestro Atlántico"],
]


class ArenasProjects:

    def __init__(self):
        self.main_endpoint = "https://arenasinmobiliaria.co/proyecto/"
        self.all_projects_by_arenas = []

    def get_projects(self) -> list:
        for project in list_endpoint:
            # Get the url to start scraping
            response_b = requests.get(f"{self.main_endpoint}{project[0]}")
            track_logs(f"{self.main_endpoint}{project[0]}")
            
            soup_b = BeautifulSoup(response_b.text, "html.parser")
            # get url of website
            website = f"{self.main_endpoint}{project[0]}"
            # get the name of project
            name = soup_b.find(name="h1", class_="elementor-heading-title elementor-size-default").text
            # get the src of logo
            logo = soup_b.find(name="div", class_="elementor-widget-container").select_one("img").get("src")
            # get the location of project from list 'list_endpoint'
            location = project[3]
            # get the area in m2 of apartment
            area = soup_b.find(name="span", class_="elementor-icon-list-text").text.split(",")[0]
            # get the city of project from list 'list_endpoint'
            city = project[2]
            # get the type of project from list 'list_endpoint'
            type = project[1]
            # get the address of salesroom and the contact to ask information
            try:
                address = soup_b.find(name="div", class_="elementor-element elementor-element-51cd7e6 e-con-full e-flex e-con e-child").select("div")[0].text.split(":")[1].split("-")[0]
                contact = soup_b.find(name="div", class_="elementor-element elementor-element-aa067cf elementor-widget elementor-widget-text-editor").select_one("a").text.split("App")[1]
            except IndexError:
                address = "no found"
                contact = "no found"
            # get the src of background of project
            img_url = soup_b.find(name="a", class_="e-gallery-item elementor-gallery-item elementor-animated-content").get("href")
            # get a summary about the project
            description = soup_b.find(name="div", class_="elementor-element elementor-element-c3c4bd2 elementor-widget elementor-widget-theme-post-content").select_one("p").text
            # get the price of project in COP
            try:
                price = soup_b.find(name="div", class_="elementor-element elementor-element-14ee783 elementor-widget elementor-widget-heading").select_one("span").text.split("$")[1].replace(".", "")
            except IndexError:
                price = int(soup_b.find(name="div", class_="elementor-element elementor-element-14ee783 elementor-widget elementor-widget-heading").select_one("span").text.split("S")[0])*1300000

            # make the dictionary with each item scraped
            arenas_inmmob_dict = {
                "name": name,
                "logo": logo,
                "location": location,
                "city": city,
                "company": "Arenas inmobiliarias",
                "address": address,
                "contact": contact,
                "area": area,
                "price": price,
                "type": type,
                "img_url": img_url,
                "description": description,
                "url_website": website
            }
            self.all_projects_by_arenas.append(arenas_inmmob_dict)

        return self.all_projects_by_arenas

