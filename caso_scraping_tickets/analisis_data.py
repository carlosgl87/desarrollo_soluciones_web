import json

with open('data.txt') as json_file:
    data = json.load(json_file)

len_lista = len(data['_embedded']['events'])
lista_ids = []
lista_precios = []
for i in range(len_lista):
    lista_ids.append(data['_embedded']['events'][i]['id'])
    lista_precios.append(data['_embedded']['events'][i]['priceRanges'][0]['min'])
print(lista_ids)
print(lista_precios)

## crear gráfico
import matplotlib.pyplot as plt
f=plt.figure()
ax=f.add_subplot(1,1,1)
ax.bar(lista_ids,lista_precios)
plt.show()
