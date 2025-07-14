#Chad Collard
#Chapter 12 Lab 3
#7/12/2025
#Weather app


import requests

# https://api.openweathermap.org/data/2.5/weather?zip=43512,us&appid=80e3bd3ae92a57f438be3823b5d9d234

response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=43512,us&units=imperial&appid=80e3bd3ae92a57f438be3823b5d9d234")

if response:
    response_dict = response.json()
    print('The Current Weather for', response_dict['name'],':')
    print('Conditions:', response_dict['weather'] [0] ['description'],)
    print('Temperature:', response_dict['main'] ['temp'], 'degrees')
    print('Feels Like:', response_dict['main'] ['feels_like'], 'degrees')
    print('Humidity:', response_dict['main'] ['humidity'],'%')
    print('Wind:', response_dict['wind']['speed'], 'knots @', response_dict['wind']['deg'], 'degrees')

    
