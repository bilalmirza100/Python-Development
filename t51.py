import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.speedtest.net/"
EMAIL = "nawabmirza174@gmail.com"
PASSWORD = "Zehan2910$"
PHONE = "+923212798628"
PROMISED_DOWN = 10
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 25)
        self.down = "0"
        self.up = "0"

    def get_internet_speed(self):
        print("Step 1: Opening Speedtest...")
        self.driver.get(URL)

        # Close cookie banner if present
        try:
            cookie_btn = WebDriverWait(self.driver, 4).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_btn.click()
        except Exception:
            pass

        # Click GO
        print("Step 2: Starting speed test...")
        start_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.start-button, .start-text"))
        )
        start_btn.click()

        # Wait for speed test to run completely
        print("Step 3: Waiting 55 seconds for test completion...")
        time.sleep(55)

        # Extract values safely with try/except fallbacks
        try:
            self.down = self.driver.find_element(By.XPATH, "//span[contains(@class, 'download-speed')]").text.strip()
            self.up = self.driver.find_element(By.XPATH, "//span[contains(@class, 'upload-speed')]").text.strip()
        except Exception:
            print("Notice: Primary class selectors failed, grabbing fallback result text...")
            # Fallback text grab from page result container
            results = self.driver.find_elements(By.CLASS_NAME, "result-data-value")
            if len(results) >= 2:
                self.down = results[0].text.strip()
                self.up = results[1].text.strip()

        print(f"Recorded Speeds -> Download: {self.down} Mbps | Upload: {self.up} Mbps")

    def tweet_at_provider(self):
        print("Step 4: Opening Twitter/X...")
        self.driver.get("https://x.com/i/flow/login")

        # 1. Enter Email / Username
        email_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username"]'))
        )
        email_input.send_keys(EMAIL)

        next_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))
        )
        next_btn.click()

        # 2. Verification Step (if Twitter requests phone/username confirmation)
        try:
            verify_input = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '//input[@data-testid="ocfEnterTextTextInput"]'))
            )
            verify_input.send_keys(PHONE)
            self.driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        except Exception:
            pass

        # 3. Enter Password
        pwd_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
        )
        pwd_input.send_keys(PASSWORD)

        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]'))
        )
        login_btn.click()

        # 4. Post Tweet
        print("Step 5: Drafting and posting tweet...")
        tweet_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0"]'))
        )
        message = f"Hey ISP, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_box.send_keys(message)

        post_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]'))
        )
        post_btn.click()
        print("Done! Complaint tweet posted.")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()