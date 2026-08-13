from datetime import datetime
import os
from dotenv import load_dotenv
import requests

# Load environment variables (Sheety credentials) from text file
load_dotenv(r"d:\Python\t38env.txt")

GOOGLE_SHEET_NAME = "sheet1"
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

# Get exercise details directly via manual input
exercise_name = input("Which exercise did you do? : ")
duration_min = float(input("How many minutes did it last? : "))
calories_burned = float(input("How many calories did you burn? : "))

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Prepare data payload for Sheety
sheet_inputs = {
    GOOGLE_SHEET_NAME: {
        "date": today_date,
        "time": now_time,
        "exercise": exercise_name.title(),
        "duration": duration_min,
        "calories": calories_burned,
    }
}

# Send data to Google Sheets using Sheety (Basic Auth)
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=(os.environ["ENV_SHEETY_USERNAME"], os.environ["ENV_SHEETY_PASSWORD"]),
)

"""
# Agar aap Bearer Token use karna chahte hain toh yeh use karein:
bearer_headers = {
    "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)
"""

print(f"Sheety Response: \n {sheet_response.text}")