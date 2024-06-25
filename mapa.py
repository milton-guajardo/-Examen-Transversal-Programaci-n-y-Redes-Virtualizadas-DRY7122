import geopy.distance
import googlemaps
import time

# Configura tu clave API de Google Maps
API_KEY = 'AIzaSyCspaCn5T3toneWztnsC3kHDC-RowxEaI0'

def obtener_coordenadas(ciudad, pais):
    gmaps = googlemaps.Client(key=API_KEY)
    try:
        geocode_result = gmaps.geocode(f"{ciudad}, {pais}")
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return (location['lat'], location['lng'])
        else:
            print(f"No se pudieron obtener las coordenadas de {ciudad}, {pais}.")
            return None
    except googlemaps.exceptions.ApiError as e:
        print(f"Error de API: {e}")
        return None

def calcular_distancia(coord1, coord2):
    return geopy.distance.distance(coord1, coord2).km

def obtener_duracion_viaje(origen, destino, medio_transporte):
    gmaps = googlemaps.Client(key=API_KEY)
    try:
        directions_result = gmaps.directions(origen, destino, mode=medio_transporte)
        if directions_result:
            duration = directions_result[0]['legs'][0]['duration']['text']
            return duration
        else:
            print(f"No se pudo obtener la duración del viaje de {origen} a {destino}.")
            return None
    except googlemaps.exceptions.ApiError as e:
        print(f"Error de API: {e}")
        return None

def main():
    while True:
        print("Bienvenido al calculador de distancias entre ciudades de Chile y Argentina.")
        print("Para salir, ingresa 's'.")

        ciudad_origen = input("Ciudad de Origen: ")
        if ciudad_origen.lower() == 's':
            break
        
        ciudad_destino = input("Ciudad de Destino: ")
        if ciudad_destino.lower() == 's':
            break
        
        print("Selecciona el medio de transporte:")
        print("1. Conducción (auto)")
        print("2. Caminando")
        print("3. En bicicleta")
        print("4. Transporte público")
        opcion = input("Opción (1/2/3/4): ")

        medios_transporte = {
            '1': 'driving',
            '2': 'walking',
            '3': 'bicycling',
            '4': 'transit'
        }

        if opcion not in medios_transporte:
            print("Opción no válida. Intenta de nuevo.")
            continue
        
        medio_transporte = medios_transporte[opcion]

        coord_origen = obtener_coordenadas(ciudad_origen, "Chile")
        coord_destino = obtener_coordenadas(ciudad_destino, "Argentina")

        if coord_origen and coord_destino:
            distancia_km = calcular_distancia(coord_origen, coord_destino)
            distancia_millas = distancia_km * 0.621371
            duracion = obtener_duracion_viaje(f"{ciudad_origen}, Chile", f"{ciudad_destino}, Argentina", medio_transporte)

            print(f"\nDistancia entre {ciudad_origen} y {ciudad_destino}:")
            print(f"{distancia_km:.2f} kilómetros")
            print(f"{distancia_millas:.2f} millas")
            print(f"Duración del viaje: {duracion}\n")
            
            print("Narrativa del viaje:")
            print(f"Viajar de {ciudad_origen}, Chile a {ciudad_destino}, Argentina en {medio_transporte} tomará aproximadamente {duracion}.")
        
        time.sleep(2)

if __name__ == "__main__":
    main()
