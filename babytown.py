from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)
b = driver.find_element(By.ID, "bigCookie")

while True:
  b.click()