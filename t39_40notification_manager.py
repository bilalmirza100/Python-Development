import requests

BREVO_API_KEY = "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"
SENDER_EMAIL = "nawabmirza174@gmail.com"
RECEIVER_EMAIL = "nawabmirza174@gmail.com"


class NotificationManager:

    def __init__(self):
        pass

    def send_email(self, message):
        url = "https://api.brevo.com/v3/smtp/email"
        headers = {
            "accept": "application/json",
            "api-key": BREVO_API_KEY,
            "content-type": "application/json"
        }
        payload = {
            "sender": {"name": "Flight Deal Finder", "email": SENDER_EMAIL},
            "to": [{"email": RECEIVER_EMAIL}],
            "subject": "Low Price Flight Alert!",
            "textContent": message
        }
        response = requests.post(url, json=payload, headers=headers)
        print("Email sent status:", response.status_code)