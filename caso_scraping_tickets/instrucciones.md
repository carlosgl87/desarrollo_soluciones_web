## Instrucciones caso scraping

1. Crear cuenta en ticketmaster
  - Crear una cuenta en la web https://developer.ticketmaster.com/
  - Revisar la documentación https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/ para conocer como usar el apis


2. Extraer información sobre eventos
  - Extraer información sobre 20 eventos. Para esto hacer un request a la siguiente página web https://app.ticketmaster.com/discovery/v2/events.json?size=20&apikey=iSx4TTkAfqIqhuikK6Jb3riXLPb6qJZQ

3. Guardar la información que se recibe en un archivo local
  - Para guardar la información no te olvides de hacer un dump del json


4. Analizar la estructura de la información
  - En la documentación se https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/
  Se encuentra el diccionario del json


5. Cargar la información en otro archivo ***.py*** y crear dos listas
  - La primera lista será de los ids de cada evento. La segunda lista será del precio mínimo de los ticketmaster


6. Generar un gráfico de barras de los precios mínimos de los eventos.
