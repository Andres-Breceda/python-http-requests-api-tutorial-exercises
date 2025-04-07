import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
if response.status_code == 200 :
   body = response.json()
   print(body[2]["images"][2])
else:
   print("Something went wrong")