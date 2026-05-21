"""from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
x=driver.find_element(By.XPATH,"//button[.='Copy Text']")
obj=ActionChains(driver)
obj.double_click(x).perform()
sleep(2)
driver.quit()





from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
x=driver.find_element(By.XPATH,"//div[@id='draggable']")
y=driver.find_element(By.XPATH,"//div[@id='droppable']")
obj=ActionChains(driver)
obj.drag_and_drop(x,y).perform()
sleep(2)
driver.quit()"""





























from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import Webdriverwait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
x=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
obj=ActionChains(driver)
obj.double_click(x).perform()
sleep(3)
driver.quit()
