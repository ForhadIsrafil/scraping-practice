from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://www.tripadvisor.com/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html")
time.sleep(2)
print(driver.title)

driver.find_element_by_xpath('//*[@id="component_1"]/footer/div/div/div[1]/div/div[2]/div[3]').click()
time.sleep(10)

driver.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[13]/div/div[3]')
time.sleep(5)
driver.quit()