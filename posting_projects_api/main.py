from functions.add_coordinates import add_coordinates_to_excelfile
from functions.convert_to_csv import write_to_csv
from functions.post_project_api import post_projects


list_item = ["name", "logo", "location", "city", "company", "address", "contact", "area", "price", "type", "img_url", "description", "url_website", "latitude", "longitude"]
excelfile = "overwrite_projects.xlsx"


if __name__ == "__main__":
    
    dataframe_list = add_coordinates_to_excelfile(excelfile=excelfile, list_items=list_item)
    
    write_to_csv(filename="data/projects.csv", data=dataframe_list, list_items=list_item)
    
    
    post_projects("data/projects.csv")
    
    
    
    
    