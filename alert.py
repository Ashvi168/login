from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
sleep(3)
driver.switch_to.alert.dismiss()
sleep(3)
driver.close()