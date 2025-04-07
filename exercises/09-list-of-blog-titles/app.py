import requests


response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")


def get_titles():
    if response.status_code==200:
       body = response.json()
       return  [n["title_plain"] for n in body["posts"]]
    else:
       None
    
print(get_titles())

