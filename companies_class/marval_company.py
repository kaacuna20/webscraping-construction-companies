from bs4 import BeautifulSoup
import requests


class MarvalProject:

    def __init__(self):
        self.list_by_barranquilla = []
        self.list_by_soledad = []
        # dictionary of endpoints from pagination of website
        self.dict_endpoint = {
            1: "",
            2: "page/2/",
            3: "page/3/",
            4: "page/4/"
        }

    # BY BARRANQUILLA
    def get_projects_by_barranquilla(self) -> list:
        pag = 1
        for marval_endpoint in range(4):
            # Get the url of main endpoint to start scraping
            response = requests.get(f"https://marval.com.co/resultados-de-busqueda/{self.dict_endpoint[pag]}?location%5B0%5D=barranquilla&keyword&rooms&min-price=117000000&max-price=2500000000")

            soup = BeautifulSoup(response.text, "html.parser")
            # scrap the url's of each project to get the final endpoint of each individual project
            list_projects = soup.find_all(name="div", class_="item-listing-wrap hz-item-gallery-js card")
            for project_marval in list_projects:
                # get url of website
                url_website = project_marval.find(name="h2", class_="item-title").select_one("a").get("href")
                # this particular project has a background very different from the others
                if url_website == "https://marval.com.co/proyecto/riverbay/":
                    print("riverbay do it manually")
                # exclude mega projects 'puerta Dorada' and 'Miramar' because it contents many
                # projects that subsequently appears on other pagination
                elif url_website != "https://marval.com.co/proyecto/puerta-dorada/" and url_website != "https://marval.com.co/proyecto/miramar/":
                    # Get the url to start scraping
                    response_project = requests.get(url=url_website)
                    soup_project = BeautifulSoup(response_project.text, "html.parser")

                    # get the name of project
                    name = soup_project.find(name="div", class_="page-title").select_one("h1").text
                    # get the price of project in COP
                    try:
                        price = soup_project.find(name="li", class_="item-price").text.split("$")[1].replace(",", ".")
                    except IndexError:
                        price = "no found"
                    # get if project is VIS, VIP or NO VIS
                    try:
                        type = soup_project.find(name="a", class_="hz-label label label-color-141").text.strip()
                    except AttributeError:
                        type = "No found"
                    # get the address of salesroom
                    address = soup_project.find(name="address", class_="item-address").text.strip()
                    # get the src of background of project
                    img_url = soup_project.find(name="a", class_="houzez-trigger-popup-slider-js swipebox").select_one(
                        selector="img").get("data-lazy-src")
                    # get the area in m2 of apartment
                    area = soup_project.find(name="ul", class_="list-unstyled flex-fill").select_one("strong").text.split(" ")[
                        0].replace(",", ".")
                    # get a summary about the project
                    try:
                        description = soup_project.find(name="div", class_="details-proyect-marval").select("p")[1].text
                    except IndexError:
                        try:
                            description = soup_project.find(name="div", class_="details-proyect-marval").select("p")[0].text
                        except IndexError:
                            description = None
                    # get the location of project
                    location = soup_project.find(name="address", class_="item-address").text.strip()
                    # get the url location in google map
                    url_map = soup_project.find_all(name="a", class_="icon-google")[0].get("href")

                    # make the dictionary with each item scraped
                    dict_by_project = {
                        "name": name,
                        "logo": "no found",
                        "location": location,
                        "city": "Barranquilla",
                        "company": "Marval",
                        "address": address,
                        "url_map": url_map,
                        "contact": "(607) 633 3987",
                        "area": area,
                        "price": price,
                        "type": type,
                        "img_url": img_url,
                        "description": description,
                        "url_website": url_website
                    }
                    self.list_by_barranquilla.append(dict_by_project)
            pag += 1
        return self.list_by_barranquilla

    # BY SOLEDAD
    def get_projects_by_soledad(self) -> list:
        # Get the url of main endpoint to start scraping
        response = requests.get("https://marval.com.co/resultados-de-busqueda/?location%5B%5D=soledad&keyword=&rooms=&min-price=117000000&max-price=2500000000")

        soup = BeautifulSoup(response.text, "html.parser")
        # scrap the url's of each project to get the final endpoint of each individual project
        list_projects = soup.find_all(name="div", class_="item-listing-wrap hz-item-gallery-js card")
        for project_marval in list_projects:
            # get url of website
            url_website = project_marval.find(name="h2", class_="item-title").select_one("a").get("href")
            # exclude mega projects 'Ciudad del parque' because it contents
            # many projects that subsequently appears on other pagination
            if url_website != "https://marval.com.co/proyecto/ciudad-del-parque/":
                # Get the url to start scraping
                response_project = requests.get(url=url_website)

                soup_project = BeautifulSoup(response_project.text, "html.parser")
                # get the name of project
                name = soup_project.find(name="div", class_="page-title").select_one("h1").text
                # get the price of project in COP
                try:
                    price = soup_project.find(name="li", class_="item-price").text.split("$")[1].replace(",", ".")
                except IndexError:
                    price = "Investigate"
                # get if project is VIS, VIP or NO VIS
                try:
                    type = soup_project.find(name="a", class_="hz-label label label-color-141").text.strip()
                except AttributeError:
                    type = "Investigate"
                # get the address of salesroom
                address = soup_project.find(name="address", class_="item-address").text.strip()
                # get the src of background of project
                img_url = soup_project.find(name="a", class_="houzez-trigger-popup-slider-js swipebox").select_one(
                    selector="img").get("data-lazy-src")
                # get the area in m2 of apartment
                area = soup_project.find(name="ul", class_="list-unstyled flex-fill").select_one("strong").text.split(" ")[
                    0].replace(",", ".")
                # get a summary about the project
                try:
                    description = soup_project.find(name="div", class_="details-proyect-marval").select("p")[1].text
                except IndexError:
                    try:
                        description = soup_project.find(name="div", class_="details-proyect-marval").select("p")[0].text
                    except IndexError:
                        description = None
                # get the url location in google map
                url_map = soup_project.find_all(name="a", class_="icon-google")[0].get("href")
                # get the location of project
                location = soup_project.find(name="address", class_="item-address").text.strip()

                # make the dictionary with each item scraped
                dict_by_project_soledad = {
                    "name": name,
                    "logo": "no found",
                    "location": location,
                    "city": "Soledad",
                    "company": "Marval",
                    "address": address,
                    "url_map": url_map,
                    "contact": "(607) 633 3987",
                    "area": area,
                    "price": price,
                    "type": type,
                    "img_url": img_url,
                    "description": description,
                    "url_website": url_website
                }
                self.list_by_soledad.append(dict_by_project_soledad)
        return self.list_by_soledad

