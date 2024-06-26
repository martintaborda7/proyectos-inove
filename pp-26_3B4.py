# IMPORTANTE: NO borrar los comentarios

def obtener_cambio(data, moneda):
    print("Obtener tipo de cambio de:", moneda)

    # Esta función recibe como parámetro
    # del bloque principal:
    # 1) el diccionario data 
    # 2) la moneda de la cual deseamos obtener el cambio
    
    # Deberá obtener el valor de cambio
    # utilizando data y moneda
    # y retornar el valor de cambio al programa principal 

    
    # Verificar si la moneda existe en el diccionario
    if moneda in data["rates"]:
        
        return data["rates"][moneda]
    else:
        
        return f"Error: La moneda {moneda} no se encuentra en el diccionario de datos."


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # URL a la API de exchangerate
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    # Alumno:
    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver dentro de la clave "rate"
    # se encuentran los tipos de cambio de todas las monedas
    # 2) Cada moneda es una clave (key) dentro de rate, y el tipo
    # de cambio es el valor de esa clave

    # 1) API request
    # Deberá obtener el JSON de la API request
    # y almacenarlo en una variable llamada data

    # 2) Obtener tipo de cambio
    # Deberá completar la función "obtener_cambio"
    # Debe invocar a la función obtener_cambio
    # pasando como parámetro las variables
    # data y moneda
    # Y almacenar el valor de retorno de la función
    # en una variable llamada "cambio"
    
    # Importante:
    # La función obtener_cambio deberá función
    # con cualquier valor válido que se pase
    # por parámetro para moenda

    # Comienza aquí su código
    moneda = "EUR"
    import json
    import requests
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    
    data = json.loads(response.text)
    data = response.json()
    print('Imprimir todos los tipos de cambio')
    print(json.dumps(data, indent=4))
    
    
    cambio = obtener_cambio(data, moneda)
    print(f"(tipo de cambio del euro: {cambio})")
    print("terminamos")