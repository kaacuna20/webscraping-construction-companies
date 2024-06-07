from bs4 import BeautifulSoup
from aiohttp import ClientSession
import asyncio
from track_logs.logs import track_logs

# list of endpoint of each project
list_endpoint = [
    "ventura-caribe/1579",
    "villa-jardin/2305",
    "lanai/1533",
    "makani/3059",
    "esmeralda/442",
    "moretti/2972",
    "missoni/2341"
]


class ColpatriaProject:

    def __init__(self):
        self.main_endpint = "https://constructoracolpatria.com/proyectos/vivienda/"
        self.all_projects_by_colpatria = []

    async def get_item(self, session, url: str) -> dict:
        response = await session.get(url)
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        web_site = url
        # get the name of project
        name = soup.find(name="div", class_="migas migas-vivienda migas-dk").text.split("|")[3].strip()
        # get the city
        city = soup.find(name="div", class_="migas migas-vivienda migas-dk").text.split("|")[2].strip()
        # get if project is VIS, VIP or NO VIS
        try:
            type = soup.find(name="div", class_="mns-vis vis-dk").text.upper()
        except AttributeError:
            type = "NO VIS"
            # get the price of project in COP
        price = soup.find(name="span", class_="map_price_cop activo").text.split("$")[1].strip("*").replace(".", "")
        # get the area in m2 of apartment
        area = soup.find(name="div", class_="box-txt-right fadeInRight area-proyect").text.split("desde")[1].strip(
            "m²").replace(",", ".")
        # get the src of background of project
        url_img = soup.find(name="div", id="box-galeria").select_one("img").get("src")
        # get the src of logo
        logo = soup.find(name="div", class_="fadeInRight logo-proyect").select_one("img").get("src")
        # get the address of salesroom
        address = soup.find(name="div", class_="dir-proyect").text
        # get the location of project
        location = soup.find(name="div", class_="dir-proyect sector-proyect sector-dk").text.split(":")[1]
        # get a summary about the project
        try:
            description = soup.find(name="span", class_="parrafo_desta").text
        except AttributeError:
            description = "no found"
            # get the contact to ask information
        contact = "+57 321 392 3797 - 321 345 5672 - 321 452 1163"

        # make the dictionary with each item scraped
        dict_by_project = {
            "name": name,
            "logo": logo,
            "location": location,
            "city": city,
            "company": "Colpatria",
            "address": address,
            "url_map": "no found",
            "contact": contact,
            "area": area,
            "price": price,
            "type": type,
            "img_url": url_img,
            "description": description,
            "url_website": web_site
        }
        return dict_by_project

    async def get_projects(self) -> list:
        async with ClientSession() as session:
            for project in list_endpoint:
                # Get the url to start scraping
                url = f"{self.main_endpint}{project}"
                track_logs(url)
                self.all_projects_by_colpatria.append(asyncio.create_task(self.get_item(session, url)))
                response = await asyncio.gather(*self.all_projects_by_colpatria)

        return response