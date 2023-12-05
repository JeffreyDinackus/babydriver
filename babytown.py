from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

import threading
import os

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)
b = driver.find_element(By.ID, "bigCookie")

def task1(b):
  i = 0
    while i < 500:
       b.click()
       i+=1

def task2(b):
  i = 0
    while i < 500:
       b.click()
       i+=1

t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')


t1.join()
t2.join()

  
  
