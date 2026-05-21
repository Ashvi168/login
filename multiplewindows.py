from time import sleep

import execute
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.execute_script("window.open('https://www.youtube.com/','_blank');")
x=driver.window_handles
driver.switch_to.window(x[1])
driver.find_element(By.XPATH,'//input[@name="search_query"]').send_keys("bts",Keys.ENTER)
sleep(10)
driver.quit()
