import requests

url = 'https://assets.breatheco.de/apis/fake/sample/post.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)