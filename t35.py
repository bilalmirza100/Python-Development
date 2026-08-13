import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = "98e67b211bdfe99aedcd15916e7baa5d"


BREVO_API_KEY = "your api key"
YOUR_PHONE_NUMBER = "+923212798628"

weather_params = {
    "lat": 30.0417,  
    "lon": 72.3528,   
    "appid": OWM_API_KEY,
    "cnt": 4    
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_it_rain = False

for hourly_data in weather_data["list"]:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_it_rain = True

if will_it_rain:
    brevo_sms_url = "https://api.brevo.com/v3/transactionalSMS/send"
    
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }
    
    payload = {
        "sender": "RainAlert", 
        "recipient": YOUR_PHONE_NUMBER,
        "content": "It's going to rain today. Remember to bring an umbrella ☔!",
        "type": "transactional"
    }
    
    sms_response = requests.post(brevo_sms_url, json=payload, headers=headers)
    
    if sms_response.status_code in [200, 201]:
        print("Rain alert SMS sent via Brevo!")
    else:
        print(f"Failed to send SMS: {sms_response.text}")
else:
    print("No rain expected in the upcoming forecast.")