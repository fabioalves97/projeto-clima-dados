import requests

latitude = -23.55
longitude = -46.63

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m,relative_humidity_2m",
    "timezone": "America/Sao_Paulo"
}

response = requests.get(url, params=params)

print("Status da resposta:", response.status_code)

data = response.json()

print("Chaves do JSON:", data.keys())
print("Amostra de dados (temperatura):", data['hourly']['temperature_2m'][:5])

import pandas as pd

# Pegando os dados
tempo = data['hourly']['time']
temperatura = data['hourly']['temperature_2m']
umidade = data['hourly']['relative_humidity_2m']

# Criando o DataFrame
df = pd.DataFrame({
    "data_hora": tempo,
    "temperatura_C": temperatura,
    "umidade_%": umidade
})

# Mostrando as primeiras linhas
print(df.head())
import os

# Garante que a pasta ../data exista
os.makedirs("../data", exist_ok=True)
# Salvando em CSV
df.to_csv("../data/dados_climaticos.csv", index=False)
print("✅ Arquivo CSV salvo em: data/dados_climaticos.csv")
