from select import select
from selenium import webdriver
from time import sleep
"""from selenium.webdriver.firefox.service import Service
service=Service(r"D:\drivers\geckodriver.exe")
driver=webdriver.Firefox(service=service)
driver.get("https://www.youtube.com")
sleep(5)
driver.close()




from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
Browser="chrome"
if Browser=="chrome":
  driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  driver.get("https://www.youtube.com")
  sleep(5)
else:
  driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
  driver.get("https://seleniumpractise.blogspot.com/")
  searchBox=driver.find_element(By.Class,"ENqPLc").Send_Keys("practice")
driver.maximize_window()
sleep(5)
driver.close()




























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
#driver.get("https://practice.expandtesting.com/dropdown")
driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
x=driver.find_element(By.XPATH,"//select[@id='country']")
obj=Select(x)
obj.select_by_visible_text("Japan")
sleep(3)
driver.close()





































from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://trytestingthis.netlify.app/")
sleep(2)
#driver.find_element(By.XPATH,"//input[@type='date' and @id='day']").send_keys("02/09/2001")
FILE_UPLOAD=driver.find_element(By.XPATH,"//input[@type='file']")
FILE_UPLOAD.send_keys(r"C:\Users\ashvi\Downloads\Ashwini_Beere_QA_Engineer_Resume (1).PDF")
sleep(12)
driver.close()"""


