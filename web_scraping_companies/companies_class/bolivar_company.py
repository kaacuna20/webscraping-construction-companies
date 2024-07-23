from bs4 import BeautifulSoup
import requests
from track_logs.logs import track_logs

# list that content the endpoints, url_img and url_map
list_endpoint = [
    # [endpoint, url_img, url_map]
    ["catleya-aromanzza", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-clateya-constructora-bolivar.jpg"],

    ["buho-alameda-del-rio", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-buho-alameda-rio.jpg"],

    ["brisas-del-parque", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-ajustada-2021.jpg"],

    ["manglar-ciudad-de-mallorquin", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-manglar-constructora-bolivar.jpg"],

    ["vibratto-sotavento", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/vista-aerea-vibratto-constructora-2023-tarjeta.jpg"],

    ["castellana-51", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-castellana51-constructora-bolivar-barranquilla_0.jpg%20%281%29.webp"],

    ["floresta", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-floresta-constructorabolivar.jpg"],

    ["malta-ciudad-mallorquin", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-malta-constructorabolivar_0.webp"],

    ["alameda-del-rio-maria-mulata-0", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/maria-mulata-tarjeta_0.jpg"],

    ["casas-de-portobelo", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-casas-portobelo_0.jpg"],

    ["vizcaina-aromanzza", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-vizcaina-constructora-bolivar.jpg"],

    ["cisne-alameda-del-rio", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-proyecto-alameda-del-rio.jpg"],

    ["bonavento", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-bonavento-constructora-bolivar-vivienda-barranquilla.webp"],

    ["mallorca-ciudad-de-mallorquin", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjerta-mallorca-constructorabolivar.jpg.webp"],

    ["cardenal-alameda-del-rio", "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/Tarjeta%20home%20Cardenal%201.jpg"]
]


class BolivarProjects:

    def __init__(self):
        self.main_endpoint = "https://www.constructorabolivar.com/proyectos-vivienda/barranquilla/"
        self.all_projects_by_bolivar = []

    def get_projects(self) -> list:
        for project in list_endpoint:
            # Get the url to start scraping
            response = requests.get(f"{self.main_endpoint}{project[0]}")
            
            track_logs(f"{self.main_endpoint}{project[0]}")

            soup = BeautifulSoup(response.text, "html.parser")
            # get url of website
            website = f"{self.main_endpoint}{project[0]}"
            # get the name of project
            name = soup.find(name="h1", class_="title-section-single").text.strip()
            # get a summary about the project
            description = soup.find(name="article", class_="descri-section-single").select_one("p").text
            # get the src of logo
            logo = soup.find(name="div", class_="col-md-3 col-lg-3 text-center").select_one("img").get("src")
            # get the area in m2 of apartment
            area = soup.find_all(name="div", class_="row cuadros justify-content-center")[0].select_one("p").text.split("m")[0]
            # get the price of project in COP
            price = soup.find_all(name="div", class_="row cuadros justify-content-center")[0].select("p")[4].text
            if int(price) < 1000:
                price = int(price)*1300000
            # get  the contact to ask information
            contact = "(+57) 3103157550"
            # get the city of project
            city = soup.find(name="p", class_="single-zone-items fz-18").text.split("/")[0].strip()
            # get the location of project
            location = soup.find(name="p", class_="single-zone-items fz-18").text.split("/")[1].strip()
            # get the address of salesroom and the contact to ask information
            try:
                address = soup.find_all(name="div", class_="col-md-6")[-4].select_one("article").text.split("Dirección")[1].strip()
            except IndexError:
                try:
                    address = soup.find_all(name="div", class_="col-md-6")[-5].select_one("article").text.split("Dirección")[1].strip() #soup.find_all(name="div", class_="col-md-6")[-6])
                except Exception:
                    address = "no direction"
            except AttributeError:
                address = "no direction"
            
            # get the src of project from list 'list_endpoint'
            img_url = project[1]

            # make the dictionary with each item scraped
            dict_by_project = {
                "name": name,
                "logo": logo,
                "location": location,
                "city": city,
                "company": "Bolivar",
                "address": address,
                "contact": contact,
                "area": area,
                "price": price,
                "type": "no found",
                "img_url": img_url,
                "description": description,
                "url_website": website
            }
            self.all_projects_by_bolivar.append(dict_by_project)

        return self.all_projects_by_bolivar