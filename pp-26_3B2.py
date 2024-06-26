# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # NOTA:
    # Para este desafio necesitará el archivo personas.json
    # que se encuentra en el repositorio de clase

    
    # Alumno:
    # Se le solicitará acceder a datos del
    # archivo de JSON para realizar cálculos

    # 1) Lectura de archivo
    # Leer el archivo json y almacenar todo su contenido
    # en una variable llamada data

    # 2) Explorar datos
    # Imprimir en consola o utilizar el debugger
    # para explorar los datos del JSON
    # Estudie bien su contenido y la estructura

    # 3) Calculos
    # Realice la suma total de todas las edades
    # disponible en el diccionario data
    # Almacenar el valor total en una variable
    # llamada "suma_edades"

    # Le recomendamos utilizar un bucle
    # para recorrer todas las personas registradas
    # en el diccionario y sumar sus edades

    # Comienza aquí su código
    
    import json


    with open('personas.json', 'r') as file:
     data = json.load(file)
    print("Contenido del archivo JSON:")
    print(json.dumps(data, indent=4))
    
    suma_edades = 0
    for persona in data["personas"]:
      suma_edades += persona['edad']
      
    print(f"(La suma de las edades es: {suma_edades})")
    
    



print("terminamos")