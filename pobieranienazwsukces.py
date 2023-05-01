from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
opts = Options()




website = 'https://www.otodom.pl/'


driver = webdriver.Chrome(options=opts, executable_path='chromedriver')



driver.get(website)
driver.maximize_window()

time.sleep(1)
#dostanie się do wszystkich ofert z rynku pierwotnego z Wielkopolski
cookies_acceptation = driver.find_element(by=By.XPATH, value= "//button[@id='onetrust-accept-btn-handler']")
cookies_acceptation.click()
lista_wojewodztw = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/button/div[2]')
lista_wojewodztw.click()
time.sleep(1)
woj_wielkopolskie = driver.find_element(by=By.XPATH, value = '/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/div[1]/div/div[2]/ul/li[16]/label[1]')
woj_wielkopolskie.click()
search_button = driver.find_element(by=By.XPATH, value='//*[@id="search-form-submit"]' )
search_button.click()
time.sleep(5)
rynki_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/main/div/div[1]/div/form/div[2]/div[1]/div/div/div/div[1]/div[1]/div' )
rynki_button.click()
rynek_pierwotny = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/main/div/div[1]/div/form/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div' )
rynek_pierwotny.click()
search2_button = driver.find_element(by=By.XPATH, value= '//*[@id="search-form-submit"]')
search2_button.click()
time.sleep(3)

# links = driver.find_element(by=By.XPATH, value= '/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li[1]/a/article')
# links.click()
li_elements = driver.find_elements(by=By.XPATH, value= "/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")
for li_element in li_elements:
    print(li_element.text)
# ogloszenia = driver.find_elements(by=By.XPATH, value= '//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[2]/div[1]/div/ul/li[1]/a/article/div[3]')
# ogloszenia_list = []
# for single_ogloszenie in ogloszenia:
#     cena = single_ogloszenie.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[2]/div[1]/div/ul/li[1]/a/article/div[3]/span[1]').text
#     pokoje = single_ogloszenie.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[2]/div[1]/div/ul/li[1]/a/article/div[3]/span[3]').text
#
#     oglosz_item = {
#         'cena': cena,
#         'pokoje': pokoje,
#     }
#     ogloszenia_list.append(oglosz_item)
# #
# df = pd.DataFrame(ogloszenia_list)
# print(df)

time.sleep(2)