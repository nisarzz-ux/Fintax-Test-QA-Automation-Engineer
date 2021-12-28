from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random 
import time

driver = webdriver.Chrome(executable_path="G:\Fintax-Hiring\qa-test\chromedriver.exe")
driver.get("http://localhost:6464")


for i in range(0,5):
    n = random.randint(2,100)
    input_form = driver.find_element_by_id('number')
    input_form.send_keys(n)
    input_click = driver.find_element_by_id('getFactorial')
    input_click.click()
    time.sleep(3)
    driver.refresh()

time.sleep(5)
driver.close()

