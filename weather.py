import requests
def get_weather(city):
    
    API_KEY="MY_API_KEY"
    URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"