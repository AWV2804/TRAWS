weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=40.4259&lon=-86.9081&appid=36468be155548021577d9192b9d65c6d&units=metric")
packages_json = weather_response.json()
packages_str = json.dumps(packages_json, indent=2)

lat = packages_json['coord']['lat']
print(packages_str)