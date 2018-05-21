import urllib.request
import json

url = 'https://app.ticketmaster.com/discovery/v2/events.json?size=20&apikey=iSx4TTkAfqIqhuikK6Jb3riXLPb6qJZQ'
webUrl = urllib.request.urlopen(url)
data = webUrl.read()
data = json.loads(data)
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
