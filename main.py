from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://orteil.dashnet.org/cookieclicker/"

# Keep Chrome browser open after the program finishes
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


# Function to automate clicking the cookie and buying Grandma when the score is sufficient
def bot():
    # Extract the score
    score_text = driver.find_element(By.ID, "cookies").text
    score = int(score_text.split()[0].replace(",", ""))  # Convert score to int

    # Find the big cookie element and click it
    cookie = driver.find_element(By.ID, "bigCookie")
    # Find current score of element
    updated_price_1 = driver.find_element(By.ID, "productPrice1")
    updated_price_2 = driver.find_element(By.ID, "productPrice1")
    updated_price_3 = driver.find_element(By.ID, "productPrice1")
    if int(updated_price_1.text) < 405:
        if score < int(updated_price_1.text):
            cookie.click()
            return True
        else:
            # Attempt to purchase "Grandma" when score >= 100
            elements = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
            for element in elements:
                if "Grandma" in element.text:
                    element.click()
                    print("Grandma purchased!")
                    # return False
            return True
    else:
        if score < int(updated_price_2.text):
            cookie.click()
            return True
        else:
            # Attempt to purchase "Grandma" when score >= 100
            elements = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
            for element in elements:
                if "Farm" in element.text:
                    element.click()
                    print("Farm purchased!")
                    # return False
            return True


# Set timeout and tracker intervals
timeout = time.time() + 60 * 5  # 5 minutes from now
tracker = time.time() + 5  # 5 seconds from now

# Main loop to repeatedly check and click
should_continue = True
while should_continue:
    # Click the cookie if the score is less than 100
    should_continue = bot()

    # # Wait for 1 second before the next iteration
    # time.sleep(1)

    # Stop after the timeout
    if time.time() > timeout:
        break
