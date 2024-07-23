import csv

def write_to_csv(filename: str, data: list, list_items: list) -> None:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribir encabezados (opcional)
        writer.writerow(list_items)

        # Escribir datos
        for row in range(len(data)):
            dict_project = data[row]        
            writer.writerow(dict_project.values())



    
  