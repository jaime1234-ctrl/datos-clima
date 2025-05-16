import requests
import json
import os

API_KEY = os.environ["API_KEY"]
CIUDAD = "Tijuana"
PAIS = "MX"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={CIUDAD},{PAIS}&units=metric&appid={API_KEY}&lang=es"

response = requests.get(url)
data = response.json()

dias = {}
for item in data["list"]:
    fecha = item["dt_txt"].split(" ")[0]
    if fecha not in dias:
        dias[fecha] = {
            "temp_min": item["main"]["temp_min"],
            "temp_max": item["main"]["temp_max"],
            "descripcion": item["weather"][0]["description"],
            "icono": item["weather"][0]["icon"]
        }
    if len(dias) == 5:
        break

with open("clima.json", "w", encoding="utf-8") as f:
    json.dump(dias, f, indent=2, ensure_ascii=False)
