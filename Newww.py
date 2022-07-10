
import json
import requests

# api key/request url
url = input("Please, enter the webpage here:")
check_if_available = f"http://archive.org/wayback/available?url={url}"

# requests data from url
data = requests.get('https://api.archivelab.org/items/principleofrelat00eins')
data = data.json()
print(check_if_available)