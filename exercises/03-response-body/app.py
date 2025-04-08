import requests

url = "http-link"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Something went wrong")
