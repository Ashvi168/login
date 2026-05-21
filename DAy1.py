"""from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as FirefoxService
from selenium.webdriver.firefox.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
browser=""
if browser=="Chrome":
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/")
else:
    driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
sleep(15)
driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

browser = ""   # change to "firefox" if needed

if browser == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")

else:
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.youtube.com")

sleep(5)
driver.quit()"""

























"""from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://trytestingthis.netlify.app/")
sleep(4)
driver.find_element(By.ID,"fname").send_keys("ashwini")
sleep(4)
driver.find_element(By.ID,"lname").send_keys("beere")
sleep(4)
driver.close()"""





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Create Service object
service = Service(ChromeDriverManager().install())

# Launch browser
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
try:
    assert "Facebook" in driver.title
except:
    driver.save_screenshot("failed_test.png")
    print("failed")
driver.maximize_window()

sleep(2)

# Take screenshot
driver.save_screenshot("google_page.png")

print("Screenshot captured successfully")

sleep(2)

driver.quit()