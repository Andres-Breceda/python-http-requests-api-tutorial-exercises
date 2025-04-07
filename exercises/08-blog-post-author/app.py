import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")

if response.status_code==200:
    body = response.json()
    print(body["posts"][0]["author"]["name"]) #objeto diccionario

    #print(diccionario.keys())
   