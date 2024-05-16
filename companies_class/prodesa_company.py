from bs4 import BeautifulSoup
import requests

# BY BARRANQUILLA
# list endpoints of projects from Barranquilla
list_endpoint = [
    "alameda-del-rio/pardela",
    "arreboles",
    "villas-de-san-pablo/brisas-de-san-pablo"
]

# list logos of projects from Barranquilla
list_logos = [
    "https://alamedadelrio.co/wp-content/uploads/2021/10/PARDELA-200x67.png",
    "https://www.estrenarvivienda.com/arreboles/barranquilla",
    "https://villasdesanpablo.com/wp-content/uploads/2022/10/brisas-de-san-pablo-logo.png"
]

# list locations of projects from Barranquilla
list_locations = [
    "Alameda del rio",
    "Costa del Río",
    "caribe verde"
]

# BY SOLEDAD
# list endpoints of projects from Soledad
list_endpoint_s = [
    "san-antonio/caboa/apartamento-50m2/",
    "ciudad-de-los-suenos/armonia/"
]

# list logos of projects from Soledad
list_logos_s = [
    "https://www.estrenarvivienda.com/caoba/soledad",
    "https://www.google.es/url?sa=i&url=https%3A%2F%2Fprodesa.com%2Fproyecto-de-vivienda%2Fsoledad%2Fciudad-de-los-suenos%2Farmonia%2F&psig=AOvVaw1D88vrH-1BF3SAPpqMIyZ7&ust=1713489679584000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCMCR0dHMyoUDFQAAAAAdAAAAABAD",
]

# list locations of projects from Soledad
list_locations_s = [
    "San Antonio",
    "Ciudad de los Sueños"
]


class ProdesaProject:

    def __init__(self):
        self.all_projects_by_prodesa_barranquilla = []
        self.all_projects_by_prodesa_soledad = []
        self.main_endpoint = "https://prodesa.com/proyecto-de-vivienda/barranquilla/"
        self.main_endpoint_s = "https://prodesa.com/proyecto-de-vivienda/soledad/"

    def get_project_by_barranquilla(self) -> list:
        index = 0
        for project in list_endpoint:
            # Get the url to start scraping
            response = requests.get(f"{self.main_endpoint}{project}")

            soup = BeautifulSoup(response.text, "html.parser")
            # get url of website
            url_website = f"{self.main_endpoint}{project}"
            # get the address of salesroom
            address = soup.find(name="span", class_="project-header__location-item").text.split(":")[1]
            # get the name of project
            name = soup.find(name="h1", class_="inner-header__keyword inner-header__keyword--small white").text
            # get if project is VIS, VIP or NO VIS
            type = str(soup.find(name="h1", class_="inner-header__keyword inner-header__keyword--small white").select_one("span")).split('">')[0].split("--")[1]
            # get the city
            city = soup.find(name="span", class_="project-header__location-item").text.split("S")[0].strip()
            # get the price of project in COP
            price = soup.find(name="h2", class_="project-header__price").text.split("$")[1].split("*")[0]
            # get a summary about the project
            description = soup.find(name="p", class_="f-size18 rb-light").text.split("*")[0]
            # get the area in m2 of apartment
            area = soup.find(name="span", class_="icon-group__item").select_one("h5").text.split("desde")[1].split("m")[0]
            # get the src of background of project
            url_img = soup.find(name="section", class_="main-picture").get("style").split("url('")[1].split("')")[0]
            # get the contact to ask information
            contact = soup.find_all(name="h4", class_="office__address")[1].text.split(":")[1].split("+57")[1].replace(" ", "")
            # get the url location in google map
            try:
                url_map = soup.find_all(name="a", class_="btn btn-theme-2 btn-theme-2--large btn-theme-2--iconL-large btn-theme-2--f-location map-card__btn")[1].get("href")
            except IndexError:
                url_map = soup.find(name="a", class_="btn btn-theme-2 btn-theme-2--large btn-theme-2--iconL-large btn-theme-2--f-location map-card__btn").get("href")

            # make the dictionary with each item scraped
            dict_by_project = {
                "name": name,
                "logo": list_logos[index],
                "location": list_locations[index],
                "city": city,
                "company": "Prodesa",
                "address": address,
                "url_map": url_map,
                "contact": contact,
                "area": area,
                "price": price,
                "type": type,
                "img_url": url_img,
                "description": description,
                "url_website": url_website
            }
            index += 1
            self.all_projects_by_prodesa_barranquilla.append(dict_by_project)
        return self.all_projects_by_prodesa_barranquilla

    def get_project_by_soledad(self) -> list:
        index = 0
        for project in list_endpoint_s:
            # Get the url to start scraping
            response_s = requests.get(f"{self.main_endpoint_s}{project}")

            soup = BeautifulSoup(response_s.text, "html.parser")
            # get url of website
            url_website = f"{self.main_endpoint_s}{project}"
            # get the address of salesroom
            try:
                address = soup.find(name="span", class_="project-header__location-item").text.split(":")[1]
            except IndexError:
                address = soup.find(name="span", class_="project-header__location-item").text
            # get the name of project
            try:
                name = soup.find(name="h1",
                                 class_="inner-header__keyword inner-header__keyword--small white rb-light").text
            except AttributeError:
                name = soup.find(name="h1", class_="inner-header__keyword inner-header__keyword--small white").text.split("-")[0]
            # get if project is VIS, VIP or NO VIS
            try:
                type = str(soup.find(name="h1",
                                     class_="inner-header__keyword inner-header__keyword--small white rb-light").select_one(
                    "span")).split('">')[0].split("--")[1]
            except AttributeError:
                type = \
                str(soup.find(name="h1", class_="inner-header__keyword inner-header__keyword--small white").select_one(
                    "span")).split('">')[0].split("--")[1]
            # get the city
            city = soup.find(name="span", class_="project-header__location-item").text.split("S")[0].strip()
            # get the price of project in COP
            price = soup.find(name="h2", class_="project-header__price").text.split("$")[1].split("*")[0]
            # get a summary about the project
            description = soup.find(name="p", class_="f-size18 rb-light").text.split("*")[0]
            # get the area in m2 of apartment
            try:
                area = \
                soup.find(name="span", class_="icon-group__item").select_one("h5").text.split("desde")[1].split("m")[0]
            except AttributeError:
                area = soup.find(name="h3", class_="icon-title orange mb10").text
            # get the src of background of project
            url_img = soup.find(name="section", class_="main-picture").get("style").split("url('")[1].split("')")[0]
            # get the contact to ask information
            contact = soup.find_all(name="h4", class_="office__address")[1].text.split(":")[1].split("+57")[1].replace(
                " ", "")
            # get the url location in google map
            try:
                url_map = soup.find_all(name="a",
                                        class_="btn btn-theme-2 btn-theme-2--large btn-theme-2--iconL-large btn-theme-2--f-location map-card__btn")[
                    1].get("href")
            except IndexError:
                url_map = soup.find(name="a",
                                    class_="btn btn-theme-2 btn-theme-2--large btn-theme-2--iconL-large btn-theme-2--f-location map-card__btn").get(
                    "href")

            # make the dictionary with each item scraped
            dict_by_project_sol = {
                "name": name,
                "logo": list_logos_s[index],
                "location": list_locations_s[index],
                "city": city,
                "company": "Prodesa",
                "address": address,
                "url_map": url_map,
                "contact": contact,
                "area": area,
                "price": price,
                "type": type,
                "img_url": url_img,
                "description": description,
                "url_website": url_website
            }
            index += 1
            self.all_projects_by_prodesa_soledad.append(dict_by_project_sol)
        return self.all_projects_by_prodesa_soledad



