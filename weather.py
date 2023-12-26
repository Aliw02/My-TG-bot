import requests, json
from decouple import config


WEATHER_API_KEY = config('WEATHER')
weather = ['الطقس', 'درجة حرارة', "الضغط", "weather", "pressure"]

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


class City:
    def __init__(self,name,lon,lat):
        self.name = name #name of the city
        self.lon = lon #longitude 
        self.lat = lat #latitude

#تكدر تعرف اي مدينة من هذا الكلاس

basra = City("Basra, IQ","47.783489","30.508102")

baghdad = City("Baghdad, IQ","44.361488","30.508102")

najaf = City(name="Najaf, IQ",lon="44.2000", lat="32.0000" )



limit = 5
URL = BASE_URL + "lat=" + najaf.lat + "&lon=" + najaf.lon +"&lang=ar"+"&units=metric"+ "&appid=" + WEATHER_API_KEY
URL2 = BASE_URL + "lat=" + baghdad.lat + "&lon=" + baghdad.lon +"&lang=ar"+"&units=metric"+ "&appid=" + WEATHER_API_KEY
URL3 = BASE_URL + "lat=" + basra.lat + "&lon=" + basra.lon +"&lang=ar"+"&units=metric"+ "&appid=" + WEATHER_API_KEY
# URL4 = URL + URL2 + URL3
# HTTP request
najaf_rep = ['Najaf', "najaf", "النجف الأشرف", "النجف", "نجف"]
basra_rep = ["basra".lower(), "البصره", "البصرة", "بصره", "بصرة"]
def getCurrentWeather(message):
    
    if message in najaf_rep:
        response = requests.get(URL)
    elif message == 'baghdad' or message == "بغداد":
        response = requests.get(URL2)
        
    elif message in basra_rep:
        response = requests.get(URL3)
    
    # elif message == "الطقس" or message == "weather".lower():
    #     response = requests.get(URL4)
    # checking the status code of the request
    if response.status_code == 200:
    # getting data in the json format
        data = response.json()

        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        # print(f"{CITY:-^30}")
        # print(f"temp : {temperature} °C")
        # print(f"humind : {humidity} %")
        # print(f"pressure : {pressure} hPa")
        # print(f"report : {report[0]['description']} ")
        
        return f""" \n
        {message.capitalize()}, IQ \n
        درجة الحرارة : {temperature} °C\n
        الرطوبة : {humidity} %\n
        الضغط : {pressure} hPa\n
        {report[0]['description']}

        
        """
    else:
        # showing the error message
        print("Error in the HTTP request")