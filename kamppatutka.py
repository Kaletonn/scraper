import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.vuokraovi.com"
PATH = "C:\Program Files (x86)\cromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(URL)
haku = driver.find_element(By.ID, "inputLocationOrRentalUniqueNo")

haku.send_keys("lutakko")
time.sleep(1)
haku.send_keys(Keys.RETURN)

haku.send_keys("keskusta, jyväskylä")
time.sleep(1)

haku.send_keys(Keys.RETURN)
haku = driver.find_elements(By.NAME, "building.roomAmount")
driver.execute_script("arguments[0].click();", haku[3]);
haku = driver.find_element(By.ID, "surfaceMin")
haku.send_keys("55")
haku.send_keys(Keys.RETURN)
time.sleep(20)  


#kohteet = 
#time.sleep(1)
#haku.send_keys(Keys.RETURN)


#time.sleep(25)
