from dataclasses import replace
import requests
import schedule
import time
import json

# Requests data from Weather API
def pull_api():
	weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=40.4259&lon=-86.9081&appid=36468be155548021577d9192b9d65c6d&units=metric")
	weather_contents_base = str(weather_response.content)
	weather_contents_simple = weather_contents_base.replace(',',':')
	weather_contents_simple = weather_contents_simple.replace('}','')
	mod_weathercontents = (weather_contents_simple.split(':'))
	return mod_weathercontents

weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=40.4259&lon=-86.9081&appid=36468be155548021577d9192b9d65c6d&units=metric")
packages_json = weather_response.json()
packages_str = json.dumps(packages_json, indent=2)

lat = packages_json['coord']['lat']
print(lat)



def get_dew():
    dew_response = requests.get("https://api.weather.gov/gridpoints/IND/29,96")
    dew_base = str(dew_response.content)
    dew_simple = dew_base.replace('}', '')
    dew_simple = dew_simple.replace('\\n', '')
    dew_simple = dew_simple.replace(':', '')
    dew_simple = dew_simple.replace(' ', '')
    dew_simple = dew_simple.replace(',{', '')
    mod_dew = dew_simple.split('"')
    mod_loc = mod_dew.index('dewpoint')
    dew_con = float(mod_dew[mod_loc+13])
    return dew_con

# Weather condition
def get_weather():
	mod_weathercontents = pull_api()
	weather_loc = mod_weathercontents.index('[{"id"')
	weather_con = mod_weathercontents[weather_loc+1]
	return weather_con

# Temperature (deg C)
def get_temp():
	mod_weathercontents = pull_api()
	temperature_loc = mod_weathercontents.index('{"temp"')
	temperature_con = float(mod_weathercontents[temperature_loc+1])
	return temperature_con

# Feels-like Temperature (deg C)
def get_feelsliketemp():
	mod_weathercontents = pull_api()
	temperaturefeel_loc = mod_weathercontents.index('"feels_like"')
	temperaturefeel_con = float(mod_weathercontents[temperaturefeel_loc+1])
	return temperaturefeel_con

# Visibility
def get_vis():
	mod_weathercontents = pull_api()
	vis_loc = mod_weathercontents.index('"visibility"')
	visibility_con = float(mod_weathercontents[vis_loc+1])
	return visibility_con

# Wind (mph)
def get_wind():	
	mod_weathercontents = pull_api()
	wind_loc = mod_weathercontents.index('"wind"')
	wind_con = float(mod_weathercontents[wind_loc + 2])
	return wind_con

#Humidity (%)  
def get_humidity():    
	mod_weathercontents = pull_api()                                                                                                  
	humidity_loc = mod_weathercontents.index('"humidity"')                                                               
	humidity_con = float(mod_weathercontents[humidity_loc + 1]) 
	return humidity_con

def run_weather():
	weather_con = get_weather()
	temperature_con = get_temp()
	temperaturefeel_con = get_feelsliketemp()
	visibility_con = get_vis()
	wind_con = get_wind()
	humidity_con = get_humidity()
	dewpoint = get_dew()
	print("weather condition:", weather_con, "temperature:", temperature_con , "feels-like temp:",  temperaturefeel_con,  "vis:", visibility_con, "wind:", wind_con, "humidity:", humidity_con, "dewpoint:", dewpoint)  


#schedule.every(10).minutes.do(run_weather)
#while True:
	#schedule.run_pending()
	#time.sleep(1)


