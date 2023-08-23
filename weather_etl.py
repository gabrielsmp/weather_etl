import pandas as pd
import requests

# Carregar dados do arquivo CSV
data = pd.read_csv("cities.csv")

# Configurar a chave de API do OpenWeatherMap
api_key = "SUA_CHAVE_DE_API_DO_OPENWEATHERMAP"

# Função para obter dados climáticos de uma cidade
def get_weather_data(latitude, longitude):
    base_url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Lança uma exceção em caso de erro HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Erro ao obter dados climáticos:", e)
        return None

# Função para fornecer recomendações com base nas condições climáticas
def get_weather_recommendation(temperature, weather_condition):
    if weather_condition == "Rain":
        return "Leve um guarda-chuva!"
    elif temperature > 25:
        return "Está quente lá fora. Use roupas leves e beba água."
    elif temperature < 10:
        return "Está frio lá fora. Use roupas quentes e fique aconchegante."
    else:
        return "O clima parece estar razoável. Use roupas confortáveis."

# Obter recomendação para cada cidade
for _, row in data.iterrows():
    latitude, longitude = row["lat"], row["lon"]
    
    print(f"Obtendo dados climáticos para Latitude {latitude}, Longitude {longitude}...")
    
    weather_data = get_weather_data(latitude, longitude)
    
    if weather_data:
        temperature = weather_data.get("main", {}).get("temp")
        weather_condition = weather_data.get("weather", [{}])[0].get("main")
        
        print(f"Temperatura: {temperature}°C")
        print(f"Condição: {weather_condition}")
        
        recommendation = get_weather_recommendation(temperature, weather_condition)
        print(f"Recomendação: {recommendation}")
        
    else:
        print("Não foi possível obter dados climáticos para esta cidade.")
        
    print("="*30)
