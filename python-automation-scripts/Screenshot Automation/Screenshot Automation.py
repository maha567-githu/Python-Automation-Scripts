from selenium import webdriver
import time
web=webdriver.Chrome()
web.get("https://chatgpt.com")
time.sleep(2)
web.save_screenshot("chatgpt.png")
print("done")
web.get("https://www.youtube.com")
time.sleep(2)

web.save_screenshot("youtube.png")
print("success")
web.close()