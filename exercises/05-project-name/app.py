import requests

url = "https://assets.breatheco.de/apis/fake/sample/project1.php"

response = requests.get(url)

if response.status_code == 200:
    diccionario_propiedades_objeto =response.json()
    print(diccionario_propiedades_objeto["name"])
else:
    print("Something went wrong")