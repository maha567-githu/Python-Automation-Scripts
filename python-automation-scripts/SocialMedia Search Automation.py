from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
web=webdriver.Chrome()
web.get("https://www.youtube.com")
search_box=web.find_element(By.NAME,'search_query')
search_box.send_keys("Best Python Automation Projects")

search_box.send_keys(Keys.ENTER)
input ("PRESS ENTER KEY TO CLOSE.....")
web.quit()