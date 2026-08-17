from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

GOOGLE_URL = "https://docs.google.com/forms/d/e/1FAIpQLSepfHVQvoKwAnklD2FgpwwBqnOTz4UHVi4QgX0Kw00OSdPynw/viewform?usp=sf_link"
GRAANA_URL = "https://www.graana.com/rent/property-for-rent-islamabad-1/"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

# STEP 1: Open Graana in Chrome to render JS and bypass anti-bot checks
driver.get(GRAANA_URL)
time.sleep(5)  # Allow dynamic content to load

soup = BeautifulSoup(driver.page_source, "html.parser")

# Scrape Property Links
links = []
for link in soup.find_all("a", href=lambda href: href and "/property/" in href):
    href = link['href']
    full_url = href if href.startswith("http") else f"https://www.graana.com{href}"
    if full_url not in links:
        links.append(full_url)

# Scrape Prices
prices = []
for price in soup.find_all(lambda tag: tag.name in ["span", "div"] and ("PKR" in tag.get_text() or "Rs" in tag.get_text())):
    text = price.get_text().strip()
    if "PKR" in text or "Rs" in text:
        clean_price = text.split("\n")[0].strip()
        if clean_price not in prices:
            prices.append(clean_price)

# Scrape Addresses
addresses = []
for address in soup.select('div[class*="location"], span[class*="location"], p[class*="location"]'):
    clean_address = address.get_text(strip=True)
    if clean_address and clean_address not in addresses:
        addresses.append(clean_address)

print(f"Scraped {len(links)} links, {len(prices)} prices, and {len(addresses)} addresses.")

# STEP 2: Submit data to Google Form
for address, price, link in zip(addresses, prices, links):
    driver.get(GOOGLE_URL)
    time.sleep(2)

    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(address)

    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price)

    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(link)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()