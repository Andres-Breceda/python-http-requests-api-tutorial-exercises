import requests

url = "https://www.gob.mx/curp/"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Something went wrong")