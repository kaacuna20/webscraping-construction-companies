import googlemaps
from dotenv import load_dotenv
import os


class GoogleMap:
    
    _api_key = os.getenv("GOOGLE_API")  # Reemplaza con tu clave de API

    # Realiza una búsqueda de lugar
    def get_coordinates(self, text: str) -> tuple:
        gmaps = googlemaps.Client(key=GoogleMap._api_key)
        geocode_result = gmaps.geocode(text)

        if geocode_result:
            # Extrae la latitud y longitud del primer resultado
            location = geocode_result[0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            
            return latitude, longitude
        else:
            return f"No se encontraron resultados para {text}"