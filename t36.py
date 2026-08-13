import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
BREVO_ENDPOINT = "https://api.brevo.com/v3/smtp/email"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
BREVO_API_KEY = ""

SENDER_EMAIL = "nawabmirza174@gmail.com"
RECEIVER_EMAIL = "nawabmirza174@gmail.com"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json().get("Time Series (Daily)", {})

if not data:
    raise ValueError("Error fetching stock data. Check your Alpha Vantage API key or limits.")

data_list = [value for (key, value) in data.items()]

yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"

diff_percent = round((difference / yesterday_closing_price) * 100, 2)
print(f"Calculated Percentage Change for {STOCK_NAME}: {diff_percent}%")

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json().get("articles", [])


    three_articles = articles[:3]


    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n\nHeadline: {article['title']}\n\nBrief: {article['description']}"
        for article in three_articles
    ]


    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json",
    }

    for article_text in formatted_articles:
        payload = {
            "sender": {"name": "Stock Price Tracker", "email": SENDER_EMAIL},
            "to": [{"email": RECEIVER_EMAIL}],
            "subject": f"🚨 {STOCK_NAME} Alert: {up_down} {diff_percent}% Change",
            "htmlContent": f"<p style='font-family: Arial, sans-serif; white-space: pre-line;'>{article_text}</p>",
        }


        brevo_response = requests.post(BREVO_ENDPOINT, json=payload, headers=headers)

        if brevo_response.status_code == 201:
            print("Email alert successfully sent via Brevo!")
        else:
            print(f"Failed to send email. Response: {brevo_response.text}")
else:
    print(f"Percentage change ({diff_percent}%) did not meet the threshold.")