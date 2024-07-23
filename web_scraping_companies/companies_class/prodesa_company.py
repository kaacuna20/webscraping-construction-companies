from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from track_logs.logs import track_logs
import time

def fetch_html_with_selenium(url: str) -> str:
    """
    To handle pages that rely on JavaScript, you need 
    can execute JavaScript with Selenium to fetch and parse the HTML content:

    """
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Fetch the page
    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to load content (adjust as needed)

    # Get the HTML content
    html_content = driver.page_source
    driver.quit()
    return html_content

# list endpoints of projects
# this order of this list is the same order in other list's acording the project
list_endpoint = [
    "proyecto-vivienda-armonia",
    "proyecto-vivienda-caoba",
    "proyecto-vivienda-brisas-san-pablo",
    "proyecto-vivienda-pardela"
]

list_logos = [
    "https://viviendas.lahipotecaria.com/colombia/wp-content/uploads/2020/12/prodesa.png",
    "https://www.estrenarvivienda.com/sites/default/files/node-project/field-project-logo/logos_proyectos_prodesa-1-44_page-0006.jpg",
    "https://villasdesanpablo.com/wp-content/uploads/2022/10/brisas-de-san-pablo-logo.png",
    "https://alamedadelrio.co/wp-content/uploads/2021/10/PARDELA-200x67.png"
]

list_locations = [
    "ciudad de los sueños",
    "san antonio",
    "caribe verde",
    "Costa del Río",
]

list_type = [
    "VIS",
    "VIP",
    "VIP",
    "NO VIS"
]

class ProdesaProject:
    def __init__(self):
        self.all_projects_by_prodesa = []
        self.main_endpoint = "https://prodesa.com/internaproyecto/"

    def get_projects(self) -> list:
        index = 0
        for project in list_endpoint:
            # Get the url to start scraping

            html_content = fetch_html_with_selenium(url=f"{self.main_endpoint}{project}")

            # Parse with BeautifulSoup
            soup = BeautifulSoup(html_content, "html.parser")

            # get url of website
            url_website = f"{self.main_endpoint}{project}"
            track_logs(url_website)
            # get the address of salesroom
            try:
                address = soup.find(name="p", class_="text_p__bLx50 mt-0 mb-0 color-gris text_textosApis__dF4dc").text
            except:
                address = "No found"
            print(address)
            # get the name of project text_h1__tRi4t roboto text-start color-gris text_h2__hoAPK
            name = soup.find(name="h1", class_="text_h1__tRi4t roboto text-start color-gris text_h2__hoAPK").text
            # get the city
            city = soup.find(name="div", class_="BannerProyecto_stylegrupo__pE4sL pb-3").select_one("p").text
            # get the price of project in COP
            price = soup.find(name="h2", class_="text_h2__hoAPK roboto text-start color-naranja mb-0").text.split("/")[0].strip().split("Desde")[1].split("*")[0].replace(".", "")
            # get a summary about the project
            description = soup.find(name="p", class_="text_p__bLx50 color-gris text_textosApis__dF4dc").select_one("span p").text
            # get the area in m2 of apartment
            area = soup.find(name="h2", class_="text_h2__hoAPK roboto text-start color-naranja mb-0").text.split("/")[1].strip().split("Desde")[1].split("m2")[0].replace(",", ".")
            # get the src of background of project
            try:
                url_img = soup.find(name="img", class_="w-100 h_auto_img w-100 BannerProyecto_mx_height__yJC_i BannerProyecto_border_img__xGO4J").get("src")
            except AttributeError:
                url_img = "no found"
                
            contact = "(601) 3139040/ (601) 3139040"

            # make the dictionary with each item scraped
            dict_by_project = {
                "name": name,
                "logo": list_logos[index],
                "location": list_locations[index],
                "city": city,
                "company": "Prodesa",
                "address": address,
                "contact": contact,
                "area": area,
                "price": price,
                "type": list_type[index],
                "img_url": url_img,
                "description": description,
                "url_website": url_website
            }
            index += 1
            self.all_projects_by_prodesa.append(dict_by_project)
        return self.all_projects_by_prodesa



