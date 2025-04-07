import requests

def get_post_tags(post_id):
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    if response.status_code==200:
       body = response.json()
       #print([n["id"] for n in body["posts"] ]) Id"s
       resultado = [n["tags"] for n in body["posts"] if n["id"] == post_id]
       return resultado[0]
    else:
       None

print(get_post_tags(146))

