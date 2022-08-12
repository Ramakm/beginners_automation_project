#install a module pip install requests
import requests
import json

#got to website https://openweathermap.org/ create an account and find out the API key.

API_keys = "0ceaede22a520a76993abc4cee754ac1"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name:")

#Requesting the site and asking two query: 1 is API keys and another query is city for which i need to see the weather.

requests_url = f"{BASE_URL}?appid={API_keys}&q={city}"

respone = requests.get(requests_url)

#Check the status code of this response: 200 means successful, 404 means bad request. 
if respone.status_code == 200:
    data = respone.json() #if successful we want the data associated with that response ina json file..
    weather= data['weather'][0]["description"]
    print(weather)
    temprature = data["main"]["temp"]-273.15
    print(temprature)
else:
    print("An error occured")