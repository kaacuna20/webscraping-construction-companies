import os
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, WebDriverException
import requests
import time
# Import the companies class
from amarilo_company import AmariloProject
from bolivar_company import BolivarProjects
from prodesa_company import ProdesaProject
from colpatria_company import ColpatriaProject
from conaltura_company import ConalturaProject
from marval_company import MarvalProject
from others_company import OtherProjects
from arenas_inmobiliarias_company import ArenasProjects
from dotenv import load_dotenv

load_dotenv(".env")

# ALL PROJECTS CLASS
amarilo_projects = AmariloProject()
marval_projects = MarvalProject()
bolivar_projects = BolivarProjects()
prodesa_projects = ProdesaProject()
colpatria_projects = ColpatriaProject()
conaltura_projects = ConalturaProject()
arenas_inmobiliarias_projects = ArenasProjects()
others_projects = OtherProjects()

# open Excel file
workbook = openpyxl.load_workbook("projects.xlsx")

# Create sheets with the name of companies
# worksheet = by default is 'amarilo'
worksheet1 = workbook.create_sheet("marval")
worksheet2 = workbook.create_sheet("arenas_inmobiliaria")
worksheet3 = workbook.create_sheet("bolivar")
worksheet4 = workbook.create_sheet("colpatria")
worksheet5 = workbook.create_sheet("conaltura")
worksheet6 = workbook.create_sheet("prodesa")
worksheet7 = workbook.create_sheet("others")


# write the data for each sheet
# Amarilo
worksheet = workbook["amarilo"]
row_cell = 2
for record_project in amarilo_projects.get_projects():
    colum_cell = 1
    for data in record_project:
        worksheet.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Conaltura
worksheet5 = workbook["conaltura"]
row_cell = 2
for record_project in conaltura_projects.get_projects():
    colum_cell = 1
    for data in record_project:
        worksheet5.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Bolivar
worksheet3 = workbook["bolivar"]
row_cell = 2
for record_project in bolivar_projects.get_projects():
    colum_cell = 1
    for data in record_project:
        worksheet3.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Arenas Inmobiliaria
worksheet2 = workbook["arenas_inmobiliaria"]
row_cell = 2
for record_project in arenas_inmobiliarias_projects.get_projects():
    colum_cell = 1
    for data in record_project:
        worksheet2.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Colpatria
worksheet4 = workbook["colpatria"]
row_cell = 2
for record_project in colpatria_projects.get_projects():
    colum_cell = 1
    for data in record_project:
        worksheet4.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Prodesa
worksheet6 = workbook["prodesa"]
row_cell = 2
for record_project in prodesa_projects.get_project_by_soledad():
    colum_cell = 1
    for data in record_project:
        worksheet6.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1
for record_project in prodesa_projects.get_project_by_barranquilla():
    colum_cell = 1
    for data in record_project:
        worksheet6.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Marval
worksheet1 = workbook["marval"]
row_cell = 2
for record_project in marval_projects.get_projects_by_soledad():
    colum_cell = 1
    for data in record_project:
        worksheet1.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1
for record_project in marval_projects.get_projects_by_barranquilla():
    colum_cell = 1
    for data in record_project:
        worksheet1.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Others
worksheet7 = workbook["others"]
row_cell = 2
for record_project in others_projects.ACF:
    colum_cell = 1
    for data in record_project:
        worksheet7.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1
for record_project in others_projects.APIROS:
    colum_cell = 1
    for data in record_project:
        worksheet7.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1
for record_project in others_projects.COCONCRETO:
    colum_cell = 1
    for data in record_project:
        worksheet7.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1
for record_project in others_projects.OPINA_CIA:
    colum_cell = 1
    for data in record_project:
        worksheet7.cell(row=row_cell, column=colum_cell, value=record_project[data].strip())
        colum_cell += 1
    row_cell += 1

# Save the changes
workbook.save("projects.xlsx")


# CREATE THE BOT WITH SELENIUM TO WRITE THE DATA SCRAPED IN THE FORM GOOGLE
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# list of name of each sheet of Excel file
print(workbook.sheetnames)
# List of sheets: ['amarilo', 'marval', 'arenas_inmobiliaria', 'bolivar', 'colpatria', 'conaltura', 'prodesa', 'others']
iter_img = 1
iter_logo = 1
for sheet_project in workbook.sheetnames:
    worksheet = workbook[sheet_project]
    print(worksheet)
    # get the values of column 1 (item=name) and column 12 (item=img_url) and add them in a dictionary
    dict_img_url = {worksheet.cell(row=row_cell, column=1).value: worksheet.cell(row=row_cell, column=12).value for row_cell in range(2,  worksheet.max_row)}

    # get the values of column 1 (item=name) and column 12 (item=logo) and add them in a dictionary
    dict_logo = {worksheet.cell(row=row_cell, column=1).value: worksheet.cell(row=row_cell, column=2).value for row_cell in range(2,  worksheet.max_row)}
    # now we iterate on both dictionaries, to get the url's, open driver and download the html element tag_name='img'
    for name_project in dict_img_url:
        try:
            driver.get(url=dict_img_url[name_project])
            time.sleep(2)
            img = driver.find_element(By.TAG_NAME, value="img")

            with open(f'static/images/background/{iter_img}-{sheet_project}-{name_project.strip()}.png', 'wb') as file:
                file.write(img.screenshot_as_png)

        except InvalidArgumentException:
            print(f"{iter_img}-{sheet_project} could not download")

        except NoSuchElementException:
            print(f"{iter_img}-{sheet_project}  could not download")

        except WebDriverException:
            print("url no found")

        iter_img += 1

    for name_project in dict_logo:
        try:
            driver.get(url=dict_logo[name_project])
            time.sleep(2)
            img = driver.find_element(By.TAG_NAME, value="img")

            with open(f'static/images/logos/{iter_logo}-{sheet_project}-{name_project.strip()}.png', 'wb') as file:
                file.write(img.screenshot_as_png)

        except InvalidArgumentException:
            print(f"{iter_logo}-{sheet_project} could not download")

        except NoSuchElementException:
            print(f"{iter_logo}-{sheet_project}  could not download")

        except WebDriverException:
            print("url no found")

        iter_logo += 1

driver.close()

# SEND POST REQUEST USING THE API THAT WAS CREATED IN PROJECT "HOUSE PROJECT SEARCHING"
# create a list of tag column
list_item = ["name", "logo", "location", "city", "company", "address", "url_map", "contact",
             "area", "price", "type", "img_url", "description", "url_website"]

# get a valid apikey and the endpoint to make the 'POST' request
API_KEY = os.getenv("ADMI_APIKEY")
# This is the server, this can change
SERVER = "http://127.0.0.1:5002/"
URL = f"{SERVER}add"

# create a dictionary of parameters according to API Documentation
parameters = {}
# create a loop for since the first until last row of each sheet
for row_record_project in range(2, worksheet.max_row + 1):
    # create a loop for since the first until last column of each record
    for item in range(0, worksheet.max_column):
        # write the parameters with the values getting from Excel document
        parameters["api_key"] = API_KEY
        parameters[list_item[item]] = worksheet.cell(row=row_record_project, column=item + 1).value
    # Sent the POST requests
    response = requests.post(url=URL, params=parameters)
    # watch the response
    print(response.text)





