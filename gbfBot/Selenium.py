import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Open browser
driver = webdriver.Chrome()  # Use appropriate WebDriver
driver.get("https://game.granbluefantasy.jp/#mypage")

# Find button and click
# Use ID, class, name, etc.
time.sleep(50)
button = driver.find_element(By.CLASS_NAME, "btn-link-multibattlelist se-ok")
button.click()
time.sleep(10)

# Close browser after execution
driver.quit()
