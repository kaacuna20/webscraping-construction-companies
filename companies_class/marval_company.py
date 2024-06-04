from bs4 import BeautifulSoup
import requests
from track_logs.logs import track_logs


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
        
        index = 0
        
        list_url_logos = [
            "https://www.estrenarvivienda.com/sites/default/files/styles/project_brand_style/public/logo-proyectos/images/2024-04/Formato-estrenar-vivienda-imagenes.jpg?itok=isrTbI6s", #riverblue
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/palmanova-1000_1000.png", #palmanova
            "https://www.estrenarvivienda.com/sites/default/files/styles/project_brand_style/public/node-project/field-project-logo/proyecto_nuevo_-_2023-07-28t114533.849.jpg?itok=WOTxzMMW",#natura
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/proyecto_nuevo_-_2023-05-31t110253.712.jpg", #amareto
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/estrenar_vivienda_marval_ciudad_del_parque_el_cocuy-01.jpg", #cocuy
            "https://olglass.com.co/uploads/1/2020-05/CAROLINA-1000.png", #coralina
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #siena
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-ciudad-del-parque-bari.jpg", #bari
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-ciudad-del-parque-tayrona.jpg", #tayrona II
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #flamencos
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #solario
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo_dimaro.jpg", #dimaro
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/genova-logo.jpg", #genova
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-aquanova.jpg", #aquanova
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-puerta-dorada-cistalina.jpg", #cristalina
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/puerta-dorada-marismalogo.jpg", #marisma
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo100estrenarvivienda_65.jpg", #la plazuela
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #altos parque
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo100estrenarvivienda_67.jpg", #vallarta
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-riserside.jpg", #riverside
            "https://www.estrenarvivienda.com/sites/default/files/styles/project_brand_style/public/node-project/field-project-logo/logo100estrenarvivienda_61.jpg?itok=CqoAubhC", #acandi
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-ciudad-del-parque-salamnca_0.jpg", #salamanca
            "https://www.estrenarvivienda.com/sites/default/files/styles/project_brand_style/public/node-project/field-project-logo/logo-ciudad-del-parque-el-nukak.jpg?itok=9wtYzOpx", #nukak
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo100estrenarvivienda_68.jpg", #bolonia
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo100estrenarvivienda_69.jpg", #firenze
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo100estrenarvivienda_64.jpg", #napoli
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/puerta-dorada-arrecofe-logo.jpg", #arrecife
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #el lago
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #la isla
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo100estrenarvivienda_60.jpg", #bahia
        ]
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
                track_logs(url_website)

                # this particular project has a background very different from the others
                if url_website == "https://marval.com.co/proyecto/riverbay/":
                    print("riverbay do it manually")
                    
                # exclude mega projects 'puerta Dorada' and 'Miramar' because it contents many
                # projects that subsequently appears on other pagination
                elif url_website == "https://marval.com.co/proyecto/puerta-dorada/" or  url_website == "https://marval.com.co/proyecto/miramar/": 
                    pass
                else:
                    # Get the url to start scraping
                    response_project = requests.get(url=url_website)
                    soup_project = BeautifulSoup(response_project.text, "html.parser")

                    # get the name of project
                    name = soup_project.find(name="div", class_="page-title").select_one("h1").text
                    # get the price of project in COP
                    try:
                        price = soup_project.find(name="li", class_="item-price").text.split("$")[1].replace(",", "")
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
                        "logo": list_url_logos[index],
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
                    index += 1
            pag += 1
        return self.list_by_barranquilla

    # BY SOLEDAD
    def get_projects_by_soledad(self) -> list:
        
        index = 0
        
        list_url_logos = [
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/estrenar_vivienda_marval_ciudad_del_parque_el_cocuy-01.jpg", #cocuy
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-ciudad-del-parque-bari.jpg", #bari
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-ciudad-del-parque-tayrona.jpg", #tayrona II
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #flamencos
            "https://marval.com.co/wp-content/uploads/2022/03/Grupo-429.png", #solario
            "https://www.estrenarvivienda.com/sites/default/files/styles/project_brand_style/public/node-project/field-project-logo/logo100estrenarvivienda_61.jpg?itok=CqoAubhC", #acandi
            "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logo-ciudad-del-parque-salamnca_0.jpg", #salamanca
            "https://www.estrenarvivienda.com/sites/default/files/styles/project_brand_style/public/node-project/field-project-logo/logo-ciudad-del-parque-el-nukak.jpg?itok=9wtYzOpx" #nukak
        ]
        
        
        # Get the url of main endpoint to start scraping
        response = requests.get("https://marval.com.co/resultados-de-busqueda/?location%5B%5D=soledad&keyword=&rooms=&min-price=117000000&max-price=2500000000")

        soup = BeautifulSoup(response.text, "html.parser")
        # scrap the url's of each project to get the final endpoint of each individual project
        list_projects = soup.find_all(name="div", class_="item-listing-wrap hz-item-gallery-js card")
        index = 0
        for project_marval in list_projects:
            # get url of website
            url_website = project_marval.find(name="h2", class_="item-title").select_one("a").get("href")
            # exclude mega projects 'Ciudad del parque' because it contents
            # many projects that subsequently appears on other pagination
            if url_website != "https://marval.com.co/proyecto/ciudad-del-parque/":
                # Get the url to start scraping
                response_project = requests.get(url=url_website)
                track_logs(url_website)

                soup_project = BeautifulSoup(response_project.text, "html.parser")
                # get the name of project
                name = soup_project.find(name="div", class_="page-title").select_one("h1").text
                # get the price of project in COP
                try:
                    price = soup_project.find(name="li", class_="item-price").text.split("$")[1].replace(",", "")
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
                    "logo": list_url_logos[index],
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
                index += 1
        return self.list_by_soledad

