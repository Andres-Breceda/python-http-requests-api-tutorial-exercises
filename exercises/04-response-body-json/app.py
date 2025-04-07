import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

if response.status_code == 200:
   tiempo = response.json()
   horas = tiempo["hours"]
   minutos = tiempo["minutes"]
   segundos = tiempo["seconds"]
   print("Hora actual: ", horas,"h", minutos,"min", segundos, "seg")
else:
   None  