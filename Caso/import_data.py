import urllib.request
import json

f = open("codigos_imdb.txt","r")
fl = f.read().splitlines()
lista_peliculas = []
for x in fl:
    lista_peliculas.append(x)
lista_data = []

#file1 = open("MyFile.txt","a")
for pel in lista_peliculas:
    url = 'http://www.omdbapi.com/?i=' + str(pel) +'&apikey=8bcf11a8'
    webUrl = urllib.request.urlopen(url)
    data = webUrl.read()
    data = json.loads(data)
    txt = 'peliculas/'+str(pel)+'.txt'
    with open(txt, 'w') as outfile:  
        print(txt)
        json.dump(data, outfile)

