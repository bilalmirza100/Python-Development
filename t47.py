import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ"
BUY_PRICE = 108.0

MY_EMAIL = "nawabmirza174@gmail.com"
MY_PASSWORD = "tdii wwhi qije gghh"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

cookies = {
    "i18n-prefs": "USD",
}

response = requests.get(URL, headers=headers, cookies=cookies)
soup = BeautifulSoup(response.content, "lxml")

price_span = soup.find(class_="a-offscreen")

if price_span:
    price_text = price_span.get_text().strip()
    
    clean_price = "".join([char for char in price_text if char.isdigit() or char == '.'])
    price = float(clean_price)
    
    print(f"Current Price: ${price}")

    if price < BUY_PRICE:
        title_tag = soup.find(id="productTitle")
        title = title_tag.get_text().strip() if title_tag else "Amazon Item"
        
        message = f"Subject: Amazon Price Alert!\n\n{title} is now ${price}\n{URL}".encode("utf-8")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=message
            )
        print("Price alert email sent successfully!")
    else:
        print(f"Price (${price}) is higher than target limit (${BUY_PRICE}). No email sent.")

else:
    print("Could not find price element. Amazon may have served a CAPTCHA page.")