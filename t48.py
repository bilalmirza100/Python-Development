from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep browser open after script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Locate the main cookie to click
cookie = driver.find_element(By.ID, value="cookie")

# Get upgrade item IDs (Cursor, Grandma, Factory, Mine, etc.)
store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in store_items if item.get_attribute("id")]

# Timers
timeout = time.time() + 5        # Check upgrades every 5 seconds
five_min = time.time() + 60 * 5  # Stop bot after 5 minutes

while True:
    cookie.click()

    # Every 5 seconds: check and buy the most expensive affordable upgrade
    if time.time() > timeout:

        # Extract current cookie count
        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Get current prices of all upgrades
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            text = price.text
            if text != "":
                # Convert text like "Cursor - 15" -> 15
                cost = int(text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Map item IDs to their respective prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Find items that are currently affordable
        affordable_upgrades = {}
        for cost, item_id in cookie_upgrades.items():
            if cookie_count >= cost:
                affordable_upgrades[cost] = item_id

        # Purchase the most expensive affordable upgrade
        if len(affordable_upgrades) > 0:
            highest_price_affordable_upgrade = max(affordable_upgrades.keys())
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(By.ID, value=to_purchase_id).click()

        # Reset 5-second timer
        timeout = time.time() + 5

    # Stop after 5 minutes and print the score
    if time.time() > five_min:
        cps = driver.find_element(By.ID, value="cps").text
        print(f"cookies/second: {cps}")
        break

driver.quit()