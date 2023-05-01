from selenium import webdriver
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, parse_qs

import csv


start_time = time.time()

import pandas as pd
opts = Options()





website = 'https://www.otodom.pl/pl/oferta/promocja-2-pokoje-37-93-m2-rataje-gotowe-ID4lcwN'


driver = webdriver.Chrome(options=opts, executable_path='chromedriver')


driver.get(website)
driver.maximize_window()
time.sleep(1)


cookies_acceptation = driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
cookies_acceptation.click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "map")))
driver.execute_script("arguments[0].scrollIntoView();", element)


time.sleep(1)
try:
    element1 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[6]/div/div/div/div[14]/div/a")))
except:
    element1 = None
try:
    element2 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div/div/div[14]/div/a")))
except:
    element2 = None
try:
    element3 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/div[6]/div/div/div/div[14]/div/a")))
except:
    element3 = None
try:
    element4 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/main/div[2]/div[2]/div[6]/div[2]/div/div/div[14]/div/a")))
except:
    element4 = None
if element1 is not None:
    localization = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div[3]/div[2]/div[6]/div/div/div/div[14]/div/a")
elif element2 is not None:
    localization = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div/div/div[14]/div/a" )
elif element3 is not None:
    localization = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div[2]/div[2]/div[6]/div/div/div/div[14]/div/a")
elif element4 is not None:
    localization = driver.find_element(by=By.XPATH, value="html/body/div[1]/main/div[2]/div[2]/div[6]/div[2]/div/div/div[14]/div/a")
else:
    print("Japierdole")
coordinates = localization.get_attribute("href")
try:
    localization_info = driver.find_element(by=By.CLASS_NAME, value="css-3te2t7").text
    print(localization_info)
except :
    print("Współrzędne dokładne")


parsed_value = urlparse(coordinates)
query_dict = parse_qs(parsed_value.query)
latitude = query_dict['ll'][0].split(',')[0]
longitude = query_dict['ll'][0].split(',')[1]

print(latitude, longitude)