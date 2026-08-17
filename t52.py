import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.instagram.com/"
USERNAME = "itx_bilal_mirza"
PASSWORD = "Bilal890$"
TARGET_ACCOUNT = "nobody_minds"


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        print("[1/3] Logging in...")
        self.driver.get(URL)

        username_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/')]"))
        )
        print("Login verified! Currently on home feed.")

    def find_followers(self):
        print(f"Step 2: Opening @{TARGET_ACCOUNT} profile...")
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")

        print("Clicking Followers link...")
        followers_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers')]"))
        )
        followers_link.click()

        
        print("Waiting for popup modal...")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )
        time.sleep(2)

        scroll_box = self.driver.find_element(
            By.XPATH, "//div[@role='dialog']//ul/parent::div | //div[@role='dialog']//div[contains(@class, '_aano')]"
        )

        
        print("Scrolling through followers...")
        for i in range(6):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box
            )
            time.sleep(2)
            print(f"Scroll {i + 1}/6 completed.")

    def follow(self):
        print("Step 3: Following accounts inside modal...")
        
        follow_buttons = self.driver.find_elements(
            By.XPATH, "//div[@role='dialog']//button[.//div[text()='Follow'] or text()='Follow']"
        )

        print(f"Found {len(follow_buttons)} target accounts.")

        for button in follow_buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                time.sleep(1)

                if "Follow" in button.text and "Following" not in button.text:
                    button.click()
                    print("Clicked Follow.")
                    time.sleep(2)  
            except Exception as err:
                print(f"Skipped button: {err}")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()