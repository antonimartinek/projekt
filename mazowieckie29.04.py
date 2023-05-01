from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, parse_qs
import csv


start_time = time.time()

import pandas as pd

opts = Options()

website = 'https://www.otodom.pl/'

driver = webdriver.Chrome(options=opts, executable_path='chromedriver')

driver.get(website)
driver.maximize_window()

time.sleep(1)
# dostanie się do wszystkich ofert z rynku pierwotnego z ..... wybierz wojewodztwo
cookies_acceptation = driver.find_element(by=By.XPATH, value="//button[@id='onetrust-accept-btn-handler']")
cookies_acceptation.click()
lista_wojewodztw = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/button/div[2]')
lista_wojewodztw.click()
time.sleep(1)
woj_wielkopolskie = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/section[1]/div/div/form/div/div[1]/div[3]/div/div[1]/div/div[2]/ul/li[3]/label[1]')
woj_wielkopolskie.click()
search_button = driver.find_element(by=By.XPATH, value='//*[@id="search-form-submit"]')
search_button.click()
time.sleep(5)
rynki_button = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/main/div/div[1]/div/form/div[2]/div[1]/div/div/div/div[1]/div[1]/div')
rynki_button.click()
rynek_pierwotny = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/main/div/div[1]/div/form/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div')
rynek_pierwotny.click()
search2_button = driver.find_element(by=By.XPATH, value='//*[@id="search-form-submit"]')
search2_button.click()
time.sleep(3)
ogloszenia_list = []
# links = driver.find_element(by=By.XPATH, value= '/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li[1]/a/article')
# //*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li[1]
li_elements = driver.find_elements(by=By.XPATH,value="/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")

pages = driver.find_elements(by=By.XPATH, value='//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]')

for j in range(2):
    time.sleep(1)
    for i in range(len(li_elements)):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article')))
        li_elements = driver.find_elements(by=By.XPATH,value="/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")
        if li_elements:
            li_elements[i].click()
        else:
            print("No elements found")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[3]/div[2]/div[2]/div/div[1]/div[2]')))
        surface = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[1]/div[2]').text
        offer_name = driver.find_element(by=By.XPATH, value=' /html/body/div[1]/main/div[3]/div[2]/header/h1').text
        rooms_number = driver.find_element(by=By.XPATH, value=' /html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[3]/div[2]').text
        standard_of_completion = driver.find_element(by=By.XPATH, value=' //*[@id="__next"]/main/div[3]/div[2]/div[2]/div/div[4]/div[2]').text
        localization_name = driver.find_element(by=By.CLASS_NAME, value='css-gx6go5').text
        prize = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div[3]/div[2]/header/strong').text
        floor_number = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[5]/div[2]').text
        rental_cost = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[7]/div[2]').text
        form_of_property = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[2]/div[2]').text
        extras = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[6]/div[2]').text
        garage = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[8]/div[2]').text
        try:
            availability = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[3]/div[2]').text
            year_of_construction = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[4]/div[2]').text
            type_of_building = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[5]/div[2]').text
            elevator = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[7]/div[2]').text
            media = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[8]/div[2]').text
            security = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[9]/div[2]').text
            building_material = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[12]/div[2]').text
            market = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[1]/div[2]').text
        except:
            availability=0
            year_of_construction=0
            type_of_building=0
            elevator=0
            media=0
            security=0
            building_material=0
            market=0

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "map")))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        for i in range(2):
            try:
                element1 = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[6]/div/div/div/div[14]/div/a")))
                break
            except:
                element1 = None
            try:
                element2 = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div/div/div[14]/div/a")))
                break
            except:
                element2 = None
            try:
                element3 = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/div[6]/div/div/div/div[14]/div/a")))
                break
            except:
                element3 = None
            try:
                element4 = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/main/div[2]/div[2]/div[6]/div[2]/div/div/div[14]/div/a")))
                break
            except:
                element4 = None
            try:
                element5 = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[4]/div/div/div/div[14]/div/a")))
                break
            except:
                element5 = None
        if element1 is not None:
            localization = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div[3]/div[2]/div[6]/div/div/div/div[14]/div/a")
        elif element2 is not None:
            localization = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div/div/div[14]/div/a")
        elif element3 is not None:
            localization = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div[2]/div[2]/div[6]/div/div/div/div[14]/div/a")
        elif element4 is not None:
            localization = driver.find_element(by=By.XPATH,value="html/body/div[1]/main/div[2]/div[2]/div[6]/div[2]/div/div/div[14]/div/a")
        elif element5 is not None:
            localization = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div[3]/div[2]/div[4]/div/div/div/div[14]/div/a")
        else:

            coordinates = "Nie znaleziono"
            print(offer_name)
        try:
            coordinates = localization.get_attribute("href")
            parsed_value = urlparse(coordinates)
            query_dict = parse_qs(parsed_value.query)
            latitude = query_dict['ll'][0].split(',')[0]
            longitude = query_dict['ll'][0].split(',')[1]
        except:
            latitude = 0
            longitude = 0

        try:
            localization_info = driver.find_element(by=By.CLASS_NAME, value="css-3te2t7").text
        except:
            localization_info = "Współrzędne dokładne"
        ogloszenia_item = {
            'surface': surface,
            'offer name': offer_name,
            'rooms ': rooms_number,
            'standard': standard_of_completion,
            'localization_name': localization_name,
            'prize': prize,
            'localization_info': localization_info,
            'latitude': latitude,
            'longitude' : longitude,
            'floor_number' : floor_number,
            'rental_cost': rental_cost,
            'form_of_property': form_of_property,
            'extras': extras,
            'garage': garage,
            'availability': availability,
            'year_of_construction': year_of_construction,
            'type_of_building': type_of_building,
            'elevator': elevator,
            'media':media,
            'security':security,
            'building_material': building_material,
            'market': market,
        }
        ogloszenia_list.append(ogloszenia_item)

        driver.back()
        time.sleep(1)
        li_elements = driver.find_elements(by=By.XPATH,value="/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")
        with open('ogloszenia.csv', mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['prize', 'surface', 'offer name', 'rooms ', 'standard', 'localization_info', 'localization_name', 'latitude',
                          'longitude', 'floor_number', 'rental_cost', 'form_of_property', 'extras', 'garage', 'availability', 'year_of_construction'
                        ,'type_of_building','elevator','media','security','building_material', 'market']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for item in ogloszenia_list:
                writer.writerow(item)

    time.sleep(2)
    button = driver.find_element(by=By.XPATH,value='//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[4]/div/nav/button[6]')
    button.click()
    time.sleep(3)

    # Scroll down
    for i in range(10):
        driver.execute_script("window.scrollBy(0, 1300)")
        time.sleep(0.2)

    # Scroll up
    for i in range(10):
        driver.execute_script("window.scrollBy(0, -1300)")
        time.sleep(0.2)
    time.sleep(2)
    li_elements = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")


for k in range(60):
    time.sleep(1)
    for i in range(len(li_elements)):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article')))
        li_elements = driver.find_elements(by=By.XPATH,value="/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")
        if li_elements:
            li_elements[i].click()
        else:
            print("No elements found")
        WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[3]/div[2]/div[2]/div/div[1]/div[2]')))
        surface = driver.find_element(by=By.XPATH,
                                      value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[1]/div[2]').text
        offer_name = driver.find_element(by=By.XPATH, value=' /html/body/div[1]/main/div[3]/div[2]/header/h1').text
        rooms_number = driver.find_element(by=By.XPATH,
                                           value=' /html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[3]/div[2]').text
        standard_of_completion = driver.find_element(by=By.XPATH,
                                                     value=' //*[@id="__next"]/main/div[3]/div[2]/div[2]/div/div[4]/div[2]').text
        localization_name = driver.find_element(by=By.CLASS_NAME, value='css-gx6go5').text
        prize = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div[3]/div[2]/header/strong').text
        floor_number = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[5]/div[2]').text
        rental_cost = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[7]/div[2]').text
        form_of_property = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[2]/div[2]').text
        extras = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[6]/div[2]').text
        garage = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[2]/div/div[8]/div[2]').text
        try:
            availability = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[3]/div[2]').text
            year_of_construction = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[4]/div[2]').text
            type_of_building = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[5]/div[2]').text
            elevator = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[7]/div[2]').text
            media = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[8]/div[2]').text
            security = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[9]/div[2]').text
            building_material = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[12]/div[2]').text
            market = driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div[1]/div[2]').text
        except:
            availability = 0
            year_of_construction = 0
            type_of_building = 0
            elevator = 0
            media = 0
            security = 0
            building_material = 0
            market = 0
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "map")))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        for i in range(2):
            try:
                element1 = WebDriverWait(driver, 1.2).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[6]/div/div/div/div[14]/div/a")))
                break
            except:
                element1 = None
            try:
                element2 = WebDriverWait(driver, 1.2).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div/div/div[14]/div/a")))
                break
            except:
                element2 = None
            try:
                element3 = WebDriverWait(driver, 1.2).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/div[6]/div/div/div/div[14]/div/a")))
                break
            except:
                element3 = None
            try:
                element4 = WebDriverWait(driver, 1.2).until(EC.presence_of_element_located(
                    (By.XPATH, "html/body/div[1]/main/div[2]/div[2]/div[6]/div[2]/div/div/div[14]/div/a")))
                break
            except:
                element4 = None
            try:
                element5 = WebDriverWait(driver, 1.2).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div[3]/div[2]/div[4]/div/div/div/div[14]/div/a")))
                break
            except:
                element5 = None
        if element1 is not None:
            localization = driver.find_element(by=By.XPATH,
                                               value="/html/body/div[1]/main/div[3]/div[2]/div[6]/div/div/div/div[14]/div/a")
        elif element2 is not None:
            localization = driver.find_element(by=By.XPATH,
                                               value="/html/body/div[1]/main/div[3]/div[2]/div[5]/div/div/div/div[14]/div/a")
        elif element3 is not None:
            localization = driver.find_element(by=By.XPATH,
                                               value="/html/body/div[1]/main/div[2]/div[2]/div[6]/div/div/div/div[14]/div/a")
        elif element4 is not None:
            localization = driver.find_element(by=By.XPATH,
                                               value="html/body/div[1]/main/div[2]/div[2]/div[6]/div[2]/div/div/div[14]/div/a")
        elif element5 is not None:
            localization = driver.find_element(by=By.XPATH,
                                               value="/html/body/div[1]/main/div[3]/div[2]/div[4]/div/div/div/div[14]/div/a")
        else:

            coordinates = "Nie znaleziono"
            print(offer_name)
        try:
            coordinates = localization.get_attribute("href")
            parsed_value = urlparse(coordinates)
            query_dict = parse_qs(parsed_value.query)
            latitude = query_dict['ll'][0].split(',')[0]
            longitude = query_dict['ll'][0].split(',')[1]
        except:
            latitude = 0
            longitude = 0

        try:
            localization_info = driver.find_element(by=By.CLASS_NAME, value="css-3te2t7").text
        except:
            localization_info = "Współrzędne dokładne"
        ogloszenia_item = {
            'surface': surface,
            'offer name': offer_name,
            'rooms ': rooms_number,
            'standard': standard_of_completion,
            'localization_name': localization_name,
            'prize': prize,
            'localization_info': localization_info,
            'latitude': latitude,
            'longitude': longitude,
            'floor_number': floor_number,
            'rental_cost': rental_cost,
            'form_of_property': form_of_property,
            'extras': extras,
            'garage': garage,
            'availability': availability,
            'year_of_construction': year_of_construction,
            'type_of_building': type_of_building,
            'elevator': elevator,
            'media': media,
            'security': security,
            'building_material': building_material,
            'market': market,
        }
        ogloszenia_list.append(ogloszenia_item)

        driver.back()
        time.sleep(1)
        li_elements = driver.find_elements(by=By.XPATH,
                                           value="/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")
        with open('ogloszenia.csv', mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['prize', 'surface', 'offer name', 'rooms ', 'standard', 'localization_info',
                          'localization_name', 'latitude', 'longitude', 'floor_number', 'rental_cost', 'form_of_property', 'extras', 'garage',
                          'availability','year_of_construction','type_of_building','elevator','media','security','building_material', 'market']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for item in ogloszenia_list:
                writer.writerow(item)

    time.sleep(2)
    element2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[4]/div/nav/button[7]')))
    button = driver.find_element(by=By.XPATH,value='//*[@id="__next"]/div[2]/main/div/div[2]/div[1]/div[4]/div/nav/button[7]')
    button.click()
    time.sleep(2)
    for i in range(10):
        driver.execute_script("window.scrollBy(0, 1300)")
        time.sleep(0.2)

    # Scroll up
    for i in range(10):
        driver.execute_script("window.scrollBy(0, -1300)")
        time.sleep(0.2)
    time.sleep(2)
    li_elements = driver.find_elements(by=By.XPATH,
                                       value="/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[2]/div[2]/ul/li/a/article")
end_time = time.time()
print("Time taken to run the program:", end_time - start_time, "seconds")


