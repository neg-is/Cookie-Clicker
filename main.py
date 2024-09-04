from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url = "https://orteil.dashnet.org/cookieclicker/"

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Wait for the language selection button to be available
try:
    # Wait up to 10 seconds for the element to be present
    language_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )

    # Click on the English language button
    language_button.click()

except Exception as e:
    print(f"An error occurred: {e}")

# Rest of your automation logic can go here

def bot():
    score = driver.find_element(By.ID, "cookies")
    print(score.text.split()[0])
    score = int(score.text.split()[0])

    cookie = driver.find_element(By.ID, "bigCookie")
    if score < 100:
        cookie.click()
        return True
    else:
        return False

score = 0
should_continue = True
while should_continue:
    bot()

