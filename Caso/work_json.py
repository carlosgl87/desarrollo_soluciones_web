import glob
import json

lista_peliculas = glob.glob("peliculas/*.txt")

def peliculas_calificacion(valor):
    lista_pel_cal = []
    for pel in lista_peliculas:
        with open(pel) as json_file:  
            data = json.load(json_file)
            if float(data['imdbRating']) >= valor:
                lista_pel_cal.append(data['Title'])
    return lista_pel_cal

#lista = peliculas_calificacion(6)
#print(lista)

def peliculas_fechas(fecha_inicial, fecha_final):
    lista_pel_fec = []
    for pel in lista_peliculas:
        with open(pel) as json_file:  
            data = json.load(json_file)
            if (float(data['Year']) >= fecha_inicial) & (float(data['Year']) <= fecha_final):
                lista_pel_fec.append(data['Title'])
    return lista_pel_fec

lista = peliculas_fechas(1930,1940)
print(lista)

