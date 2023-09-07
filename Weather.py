import requests
import json




packages_json = weather_response.json()
packages_str = json.dumps(packages_json, indent=2)

API_fields = ['weather', 'temp', 'feels_like', 'visibility', 'wind', 'humidity']

weather_con = packages_json[API_fields[0]][0]['id']
temperature = packages_json['main'][API_fields[1]]
feel_temperature = packages_json['main'][API_fields[2]]
visibility = packages_json[API_fields[3]]
wind = packages_json[API_fields[4]]['speed']
humidity = packages_json['main'][API_fields[5]]

dew_response = requests.get("https://api.weather.gov/gridpoints/IND/29,96")
dew_json = dew_response.json()
dew_str = json.dumps(dew_json, indent=2)

dew = dew_json['properties']['dewpoint']['values'][0]['value']
print(dew)
