import requests
#import json

hakusana = input("Anna hakusana: ")

pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana


try:
    vastaus = requests.get(pyyntö) #.json()
    if not vastaus.ok:
       print("jokin meni pieleen")
except Exception as e:
    pass

print("toimii")
#print(json.dumps(sarja, indent =2))
#print(vastaus[0]["show"]["name"])

""""
for sarja in sarjat:
    print(sarja["show"]["name"])

"""

