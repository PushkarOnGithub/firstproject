from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = r"D:\Tools\chromedriver.exe"
print(time.asctime())
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")
# driver.quit()
print(time.asctime())
print(driver.title)

search = driver.find_element('s')
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(5)

print(time.asctime())
driver.quit()