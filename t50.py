import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException, 
    ElementClickInterceptedException, 
    TimeoutException
)
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURATION ---
FB_EMAIL = "nawabmirza174@gmail.com"
FB_PASSWORD = ""
BUBBLE_URL = "https://bumble.com/get-started"

def run_bumble_bot():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 2
    })

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )
    
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(BUBBLE_URL)
        time.sleep(3)

        try:
            cookie_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Accept') or contains(text(), 'I accept')]"))
            )
            cookie_btn.click()
        except TimeoutException:
            pass

        main_window = driver.current_window_handle
        
        fb_login_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue with Facebook')]"))
        )
        fb_login_btn.click()
        time.sleep(2)

        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        print("Switched to Facebook Login Window:", driver.title)

        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        pass_input = driver.find_element(By.ID, "pass")

        email_input.send_keys(FB_EMAIL)
        pass_input.send_keys(FB_PASSWORD)

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        driver.switch_to.window(main_window)
        print("Switched back to main Bumble Window")

        time.sleep(5)

        try:
            accept_cookies = driver.find_element(By.XPATH, "//span[contains(text(), 'Accept')]")
            accept_cookies.click()
        except NoSuchElementException:
            pass

        print("Starting swipe/pass routine...")
        swipe_count = 0

        while swipe_count < 100: 
            try:
                pass_button = wait.until(
                    EC.element_to_be_clickable((
                        By.XPATH, 
                        "//div[@aria-label='Pass'] | //button[contains(@aria-label, 'Pass')] | //div[contains(@class, 'encounters-action--dislike')]"
                    ))
                )
                
                pass_button.click()
                swipe_count += 1
                print(f"Passed profile #{swipe_count}")
                
                time.sleep(random.uniform(1.5, 3.5))

            except ElementClickInterceptedException:
                print("Click intercepted: Dismissing pop-up or modal...")
                try:
                    continue_swiping = driver.find_element(
                        By.XPATH, 
                        "//span[contains(text(), 'Continue')] | //div[@aria-label='Close']"
                    )
                    continue_swiping.click()
                    time.sleep(1)
                except NoSuchElementException:
                    print("Unrecognized modal encountered. Pausing for manual inspection.")
                    time.sleep(5)

            except TimeoutException:
                print("Pass button not found. Profiles may still be loading or daily limit reached.")
                time.sleep(3)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("Bot run completed. Terminating browser in 10 seconds.")
        time.sleep(10)
        driver.quit()

run_bumble_bot()