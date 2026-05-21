from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# Click on Nested iFrames option
driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()

# Switch to first frame
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

# Switch to inner frame
inner_frame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inner_frame)

# Enter text inside textbox
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Ashwini")

sleep(3)

# Back to main page
driver.switch_to.default_content()

driver.quit()






