from bs4 import BeautifulSoup
from aiohttp import ClientSession
import asyncio
from track_logs.logs import track_logs

# list that content the endpoints, url_img and url_map
list_endpoint = [
    # [endpoint, url_img, url_map]
    ["catleya-aromanzza",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-clateya-constructora-bolivar.jpg",
     "https://www.google.com/maps/search/catleya-aromanzza/@10.9240937,-74.8877226,12z/data=!3m1!4b1?entry=ttu"],

    ["buho-alameda-del-rio",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-buho-alameda-rio.jpg",
     "https://www.google.com/maps/search/buho-alameda-del-rio/@10.9958256,-74.8467745,17z/data=!3m1!4b1?entry=ttu"],

    ["brisas-del-parque",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-ajustada-2021.jpg",
     "https://www.google.com/maps/search/brisas-del-parque/@10.9748791,-74.8342283,13z/data=!3m1!4b1?entry=ttu"],

    ["manglar-ciudad-de-mallorquin",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-manglar-constructora-bolivar.jpg",
     "https://www.google.com/maps/place/Conjunto+Manglar/@11.0219789,-74.849951,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef42d613ef2b683:0x2b988067cfb441b7!8m2!3d11.0219736!4d-74.8473761!16s%2Fg%2F11nffh3kj1?entry=ttu"],

    ["vibratto-sotavento",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/vista-aerea-vibratto-constructora-2023-tarjeta.jpg",
     "https://www.google.com/maps/place/Vibratto+-+Sotavento/@10.9598117,-74.8496362,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef42d695ea9d2c3:0x498353962b89cff6!8m2!3d10.9598064!4d-74.8470613!16s%2Fg%2F11qs9zc3rj?entry=ttu"],

    ["castellana-51",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-castellana51-constructora-bolivar-barranquilla_0.jpg%20%281%29.webp",
     "https://www.google.com/maps/search/castellana-51/@11.0136298,-74.8294647,18z/data=!3m1!4b1?entry=ttu"],

    ["floresta",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-floresta-constructorabolivar.jpg",
     "https://www.google.com/maps/d/viewer?mid=1wrxunNv9DTIbXC39-e2l9du7qidLmWta&femb=1&ll=10.959882873449319%2C-74.78686545&z=14"],

    ["malta-ciudad-mallorquin",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-malta-constructorabolivar_0.webp",
     "https://www.google.com/maps/place/Malta+-+Ciudad+Mallorqu%C3%ADn/@11.0245598,-74.8427503,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef42d062bf60efd:0x27d5663d312f5a8!8m2!3d11.0245545!4d-74.8401754!16s%2Fg%2F11vf3z4015?entry=ttu"],

    ["alameda-del-rio-maria-mulata-0",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/maria-mulata-tarjeta_0.jpg",
     "https://www.google.com/maps/place/Conjunto+Maria+Mulata/@10.9945207,-74.8515332,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef42da6fe708521:0x93e11584d141a516!8m2!3d10.9945154!4d-74.8489583!16s%2Fg%2F11hd_dwyn9?entry=ttu"],

    ["casas-de-portobelo",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-casas-portobelo_0.jpg",
     "https://www.google.com/maps/place/Casas+portobelo/@10.9518361,-74.8647914,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef5d3a9f6df5c9b:0x56fb42356f28eeae!8m2!3d10.9518308!4d-74.8622165!16s%2Fg%2F11tr_k7sl8?entry=ttu"],

    ["vizcaina-aromanzza",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-vizcaina-constructora-bolivar.jpg",
     "https://www.google.com/maps/search/vizcaina-aromanzza/@11.0240812,-74.816779,18.25z?entry=ttu"],

    ["cisne-alameda-del-rio",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-proyecto-alameda-del-rio.jpg",
     "https://www.google.com/maps/search/cisne-alameda-del-rio/@10.993949,-74.8486372,14z/data=!3m1!4b1?entry=ttu"],

    ["bonavento",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjeta-bonavento-constructora-bolivar-vivienda-barranquilla.webp",
     "https://www.google.com/maps/d/viewer?mid=1dSZdcnNBMuV1stU098NcmkitZBWyy42-&femb=1&ll=10.951507288299583%2C-74.84445775000002&z=14"],

    ["mallorca-ciudad-de-mallorquin",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/tarjerta-mallorca-constructorabolivar.jpg.webp",
     "https://www.google.com/maps/place/Mallorca+-+Ciudad+Mallorqu%C3%ADn/@11.0255204,-74.8426685,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef42db070a9f069:0x9d9fce0d8ee15176!8m2!3d11.0255151!4d-74.8400936!16s%2Fg%2F11vf3yt3_q?entry=ttu"],

    ["cardenal-alameda-del-rio",
     "https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/imagenes/proyectos/imagen-destacada/Tarjeta%20home%20Cardenal%201.jpg",
     "https://www.google.com/maps/place/Alameda+del+Rio/@10.9961657,-74.8430528,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef42cf0c674932b:0xcd04117053c4cf3e!8m2!3d10.9961604!4d-74.8404779!16s%2Fg%2F11c5t02ynz?entry=ttu"]
]


class BolivarProjects:

    def __init__(self):
        self.main_endpoint = "https://www.constructorabolivar.com/proyectos-vivienda/barranquilla/"
        self.all_projects_by_bolivar = []

    async def get_item(self, session, url: str, project: list) -> dict:
        response = await session.get(url)
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        # get url of website
        website = url
        # get the name of project
        name = soup.find(name="h1", class_="title-section-single").text.strip()
        # get a summary about the project
        description = soup.find(name="article", class_="descri-section-single").select_one("p").text
        # get the src of logo
        logo = soup.find(name="div", class_="col-md-3 col-lg-3 text-center").select_one("img").get("src")
        # get the area in m2 of apartment
        area = \
        soup.find_all(name="div", class_="row cuadros justify-content-center")[0].select_one("p").text.split("m")[0]
        # get the price of project in COP
        price = soup.find_all(name="div", class_="row cuadros justify-content-center")[0].select("p")[4].text
        if int(price) < 1000:
            price = int(price) * 1300000
            # get  the contact to ask information
        contact = "(+57) 3103157550"
        # get the city of project
        city = soup.find(name="p", class_="single-zone-items fz-18").text.split("/")[0].strip()
        # get the location of project
        location = soup.find(name="p", class_="single-zone-items fz-18").text.split("/")[1].strip()
        # get the address of salesroom and the contact to ask information
        try:
            address = soup.find_all(name="div", class_="col-md-6")[-4].select_one("article").text.split("Dirección")[
                1].strip()
        except IndexError:
            try:
                address = \
                soup.find_all(name="div", class_="col-md-6")[-5].select_one("article").text.split("Dirección")[
                    1].strip()  # soup.find_all(name="div", class_="col-md-6")[-6])
            except Exception:
                address = "no direction"
        except AttributeError:
            address = "no direction"

        # get the url location of project from list 'list_endpoint'
        url_map = project[2]
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
            "url_map": url_map,
            "contact": contact,
            "area": area,
            "price": price,
            "type": "no found",
            "img_url": img_url,
            "description": description,
            "url_website": website
        }
        return dict_by_project

    async def get_projects(self) -> list:
        async with ClientSession() as session:
            for project in list_endpoint:
                # Get the url to start scraping
                url = f"{self.main_endpoint}{project[0]}"
                track_logs(url)
                self.all_projects_by_bolivar.append(asyncio.create_task(self.get_item(session, url, project)))
                response = await asyncio.gather(*self.all_projects_by_bolivar)

        return response