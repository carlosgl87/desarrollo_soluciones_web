## Tutorial Caso Scraping

Para resolver el caso se desarrollaran dos archivos ***.py***.  
1. El primero será un scraper de la data que la almacenará en una carpeta.
2. El segundo codigo tendrá las funciones para analizar la información

### 1. Scraper

Para el scraper, primero se tienen que registar en la página (http://www.omdbapi.com/) y luego se podrá sacar información para cada película almacenada en el archivo codigos_imdb.txt.

```python
import urllib.request
import json

## abrir el archivo que contiene los códigos y crear una lista de todos los códigos
f = open("codigos_imdb.txt","r")
fl = f.read().splitlines()
lista_peliculas = []
for x in fl:
    lista_peliculas.append(x)
lista_data = []

# para cada elemento de la lista creada:
#    - se entrará a la url
#    - se convertirá esa información a json
#    - se guardará en un archivo dentro de una carpeta
for pel in lista_peliculas:
    url = 'http://www.omdbapi.com/?i=' + str(pel) +'&apikey=8bcf11a8'
    webUrl = urllib.request.urlopen(url)
    data = webUrl.read()
    data = json.loads(data)
    txt = 'peliculas/'+str(pel)+'.txt'
    with open(txt, 'w') as outfile:  
        print(txt)
        json.dump(data, outfile)
```

### 2. Funciones
La primera función deberá de crear una lista de películas de aquellas con calificación mayor a un número que nosotros pongamos (de 0 a 10). El código para esto deberá de:
- Crear una lista con todos los archivos que se encuentren en la carpeta donde se han guardado toda la información
- Se carará cada uno de estos archivos y se evaluará si su calificación es mayor al número que se ha definido
- De ser mayor, se guardará el título en una lista
- La función retornará la lista_data

```python
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
lista = peliculas_calificacion(6)
print(lista)
```
La otra función es similar, solo que esta vez será con fechas. Para simplificarlo, solo se trabajará con los años. Se seguirán pasos muy similares que la anterior vez

```python
import glob
import json

lista_peliculas = glob.glob("peliculas/*.txt")
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
```
