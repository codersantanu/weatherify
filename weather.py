import requests
def get_weather(city):
    
    API_KEY="MY_API_KEY"
    URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(URL)
        data=response.json()
        if response.status_code==200:
            print(f"Weather in {data['name']},{data['sys']['country']}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity :{data['main']['humidity']}%")
            print(f"Weather : {data ["Weather"][0]["description"]}")
            print(f"Wind Speed : {data['wind']['speed']} m/s")
        else:
            print(f"City{city} not found. Please check the city name and try again.")
            
    except Exception as e:
        print("Something went wrong. Please try again later.")
        
if __name__=="__main__":
    city=input("Enter city name: ")
    get_weather(city)