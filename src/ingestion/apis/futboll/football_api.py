import requests
import pandas as pd

API_URL = "https://api.football-data.org/v4/matches"
API_KEY = "TU_API_KEY"  # Regístrate en football-data.org para obtenerla

headers = {"X-Auth-Token": API_KEY}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    matches = pd.json_normalize(data['matches'])
    matches.to_csv("../../datasets/football/matches.csv", index=False)
    print("Datos guardados en datasets/football/matches.csv")
else:
    print("Error:", response.status_code, response.text)
