from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT_EMAIL = "nawabmirza174@gmail.com"
ACCOUNT_PASSWORD = "Zehan2910"
PHONE = "+923212798628"

# Configure browser options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Selenium automatically matches your Chrome v151 browser version here:
driver = webdriver.Chrome(options=chrome_options)

def abort_application():
    try:
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
    except NoSuchElementException:
        pass

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Click Reject Cookies Button
time.sleep(2)
try:
    reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
    reject_button.click()
except NoSuchElementException:
    pass

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#username, #session_key"))
)
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha: ")

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button or complex setup, skipped.")
        continue

time.sleep(5)
driver.quit()