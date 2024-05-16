import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, WebDriverException
import time


# CREATE THE BOT WITH SELENIUM TO WRITE THE DATA SCRAPED IN THE FORM GOOGLE
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
workbook = openpyxl.load_workbook("projects.xlsx")
# list of name of each sheet of Excel file
print(workbook.sheetnames)
# List of sheetnames: ['amarilo', 'marval', 'arenas_inmobiliaria', 'bolivar', 'colpatria', 'conaltura', 'prodesa', 'others']


iter_company = 1
for sheet_project in workbook.sheetnames:
    # Select the sheets from the list of workbook.sheetnames
    worksheet = workbook[sheet_project]
    print(worksheet)
    # get the values of column 1 (item=name) and column 12 (item=img_url) and add them in a dictionary
    dict_img_url = {worksheet.cell(row=row_cell, column=1).value: worksheet.cell(row=row_cell, column=12).value for row_cell in range(2,  worksheet.max_row + 1)}
    # get the values of column 1 (item=name) and column 2 (item=logo) and add them in a dictionary
    dict_logo = {worksheet.cell(row=row_cell, column=1).value: worksheet.cell(row=row_cell, column=2).value for row_cell in range(2,  worksheet.max_row + 1)}
    # now we iterate on both dictionaries, to get the url's, open driver and download the html element tag_name='img'
    iter_img = 1
    for name_project in dict_img_url:

        try:
            driver.get(url=dict_img_url[name_project])
            time.sleep(2)
            img = driver.find_element(By.TAG_NAME, value="img")

            with open(f'static/images/background1/{iter_company}.{iter_img}-{sheet_project}-{name_project.strip()}.png', 'wb') as file:
                file.write(img.screenshot_as_png)

        except InvalidArgumentException:
            print(f"{iter_company}.{iter_img}-{sheet_project}-{name_project} could not download")

        except NoSuchElementException:
            print(f"{iter_company}.{iter_img}-{sheet_project}  could not download")

        except WebDriverException:
            print(f"{sheet_project}-{name_project}  no found")

        iter_img += 1

    iter_logo = 1
    for name_project in dict_logo:
        try:
            driver.get(url=dict_logo[name_project])
            time.sleep(2)
            img = driver.find_element(By.TAG_NAME, value="img")

            with open(f'static/images/logos1/{iter_company}.{iter_logo}-{sheet_project}-{name_project.strip()}.png', 'wb') as file:
                file.write(img.screenshot_as_png)

        except InvalidArgumentException:
            print(f"{iter_company}.{iter_logo}-{sheet_project}-{name_project} could not download")

        except NoSuchElementException:
            print(f"{iter_company}.{iter_logo}-{sheet_project}-{name_project}  could not download")

        except WebDriverException:
            print(f"{sheet_project}-{name_project} no found")

        iter_logo += 1
    iter_company += 1

driver.close()








