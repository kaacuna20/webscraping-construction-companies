from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings()

# list of endpoint of each project
list_endpoint = [
    "amatista-alameda-del-rio",
    "bambu-san-antonio",
    "barranquero-alameda-del-rio",
    "brisas-del-rio-rio-alto",
    "ceiba-san-antonio",
    "corozo-san-antonio",
    "flamingo-alameda-del-rio",
    "lira-alameda-del-rio",
    "mirador-cienaga-ciudad-mallorquin",
    "monterivera-lago-alto",
    "palmar-cienaga-ciudad-mallorquin",
    "picaflor-alameda-del-rio",
    "reserva-de-la-cienaga",
    "silbador-alameda-del-rio",
    "yarumo-san-antonio"
]


class AmariloProject:

    def __init__(self):
        self.all_projects_by_amarilo = []
        self.main_endpoint = "https://amarilo.com.co/proyecto/"

    def get_projects(self) -> list:
        for project in list_endpoint:
            # Get the url to start scraping
            response = requests.get(f"{self.main_endpoint}{project}", verify=False)

            soup = BeautifulSoup(response.text, "html.parser")
            # get url of website
            url_website = f"{self.main_endpoint}{project}"
            # get the name of project
            name = soup.find(name="div", class_="title").select_one("h1").text.split(",")[1].split("-")[0]
            # get the src of logo
            logo = soup.find_all(name="div", class_="logo")[1].select_one("img").get("src")
            # get the location of project
            try:
                location = soup.find(name="div", class_="title").select_one("h1").text.split(",")[1].split("-")[1]
            except IndexError:
                location = soup.find(name="div", class_="title").select_one("h1").text.split(",")[1]
            # get the city
            city = soup.find(name="div", class_="zona").text
            # get the price of project in COP
            try:
                price = int(soup.find(name="strong", class_="jumbo").text.split(" ")[0])*1300000
            except ValueError:
                price = soup.find(name="strong", class_="jumbo").text.split("$")[1].replace(",", ".")
            # get the src of background of project
            img_url = soup.find(name="div", class_="carousel-gallery-item").select_one("img").get("src")
            # get the url location in google map
            url_map = soup.find(name="div", class_="direccion").select_one("a").get("href")
            # get the address of salesroom
            address = soup.find(name="div", class_="direccion").text
            # get a summary about the project
            try:
                descriptions = "".join([soup.find(name="div", class_="load").select("p")[item].text for item in range(3)])
            except IndexError:
                descriptions = "sin descripción"
            # get if project is VIS, VIP or NO VIS
            try:
                type = soup.find(name="div", class_="bono-wrapper").text
            except AttributeError:
                type = "NO FOUND"
            # get the area in m2 of apartment
            area = soup.find(name="div", class_="data").text.split("m")[0]
            # get the contact to ask information
            contact = "6016340000"

            # make the dictionary with each item scraped
            dict_by_project = {
                "name": name,
                "logo": logo,
                "location": location,
                "city": city,
                "company": "Amarilo",
                "address": address,
                "url_map": url_map,
                "contact": contact,
                "area": area,
                "price": price,
                "type": type,
                "img_url": img_url,
                "description": descriptions,
                "url_website": url_website
            }
            self.all_projects_by_amarilo.append(dict_by_project)

        return self.all_projects_by_amarilo
