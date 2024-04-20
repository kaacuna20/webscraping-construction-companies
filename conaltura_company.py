from bs4 import BeautifulSoup
import requests

# lists of endpoints
list_endpoint = [
    "senza",
    "bavaro",
    "catara"
]

# lists of url_map
list_url_map = [
    "url_map = https://www.google.com/maps/place/Senza+Apartamentos+Lote/@10.922718,-74.828026,15z/data=!4m6!3m5!1s0x8ef5d3be301a94ad:0xa1b1e72b8aec2340!8m2!3d10.9227177!4d-74.828026!16s%2Fg%2F11t2zd0hv2?hl=es&entry=ttu",
    "url_map = https://www.google.com/maps/place/B%C3%A1varo+Apartamentos+Conaltura/@10.9267204,-74.8284702,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef5d31be062bd25:0xed2c7fea94021b94!8m2!3d10.9267151!4d-74.8258953!16s%2Fg%2F11s38tv4z0?hl=es&entry=ttu",
    "url_map = https://www.google.com/maps/place/Catara+-+Ciudad+Mallorqu%C3%ADn/@11.0247919,-74.8479199,17z/data=!3m1!4b1!4m6!3m5!1s0x8ef42d03100f5f4f:0x7ae856a1ff1e4f4d!8m2!3d11.0247866!4d-74.845345!16s%2Fg%2F11t9hhw834?hl=es&entry=ttu"
]


class ConalturaProject:

    def __init__(self):
        self.main_endpoint = "https://conaltura.com/proyectos-de-vivienda-nueva/"
        self.all_projects_by_catara = []

    def get_projects(self):
        index = 0
        for project in list_endpoint:
            # Get the url to start scraping
            response = requests.get(f"{self.main_endpoint}{project}")

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
            price = soup.find(name="h2", class_="fz-100 font-weight-bold").text.split("$")[1].replace("'", ".")
            # get the area in m2 of apartment
            area = soup.find(name="h5", class_="text-conaltura-dark font-weight-bold descripciondetalle").text.split(" ")[0]
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
                "url_map": list_url_map[index],
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


