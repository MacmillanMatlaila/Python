import json
import requests
import sys

if len(sys.argv) != 2:
   sys.exit()
   
response = request.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

o = response.json()
for result in o["results"]:
    print(result["trackName"])