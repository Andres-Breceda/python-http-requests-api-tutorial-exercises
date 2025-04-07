import requests

def get_attachment_by_id(attachment_id):
      response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
      if response.status_code==200:
         body = response.json()
         resultado = [i['title'] for n in body['posts'] for i in n['attachments'] if i['id'] == attachment_id ]
         return resultado[0]

print(get_attachment_by_id(137))
