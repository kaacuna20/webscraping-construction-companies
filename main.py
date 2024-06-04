from driver_selenium import donwload_images_from_urls
from dataexcel import create_write_excelfile


if __name__ == "__main__":
    create_write_excelfile()
    donwload_images_from_urls(excel_file="saved_data/projects.xlsx")