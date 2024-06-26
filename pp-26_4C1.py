# IMPORTANTE: NO borrar los comentarios

import sqlite3

# https://extendsclass.com/sqlite-browser.html


# IMPORTANTE
# Debe utilizar la base de datos "libreria.db"
# que se encuentra disponible en el repositorio de clase

# Estructura de la base de datos:
# * Tabla libro *
# - id [integer] --> id del libro --> número (autoincremental)
# - titulo [text] --> Título del libro
# - cantidad_paginas [integer] --> Cantidad de páginas del libro
# - autor [text] --> Nombre del autor del libro


def get_all():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Alumno:
    # Utilizar la sentencia SELECT para obtener
    # todas las filas con todas sus columnas
    # Utilizar fetchall para obtener todos los libros
    # de la tabla
   
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute("SELECT * FROM libros;")
    libros = c.fetchall()

    conn.commit()
    conn.close()

    return libros   



def search_by_autor(autor):
    print('¡Operación búsqueda!')
    # Alumno:
    # Utilizar la sentencia SELECT para retornar
    # aquellos libros que hayan sido escritos por
    # el autor pasado por parámetro

    # De la lista de esos libros el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # titulo / cantidad_paginas

    # Retornar la lista de libros que retorna la query
    # Puede utilizar fetchall para obtener
    # todos los libros encontrados por la query
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute("SELECT titulo, cantidad_paginas FROM libros WHERE autor = ?", (autor))
    autores = c.fetchall()
    
    conn.commit()
    conn.close()
    
    return autores

def cantidad_paginas(autor):
    print(f"¿Cuántas páginas escribio {autor}?")
    # Alumno:
    # Esta función debe retornar la suma de todas
    # las páginas que escribió el autor pasado
    # por parámetro en todos sus libros
    # que haya escrito el autor

    # Puede resolverlo todo con SQL usando
    # SELECT, WHERE y SUM
    # o puede resolverlo en parte con SQL
    # y bucles

    # Esta función debe retoronar
    # la cantidad de páginas que el autor
    # a escrito en total
    # ¡DEBE RETORNAR UN ENTERO! (int)
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute("SELECT SUM(cantidad_paginas) FROM libros WHERE autor = ?", (autor,))
    resultado = c.fetchone()
    total_paginas = resultado[0] if resultado[0] is not None else 0
    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    

print(f"(BASE DE DATOS:) {get_all()})")





