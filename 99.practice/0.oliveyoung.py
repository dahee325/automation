from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

URL = 'https://www.oliveyoung.co.kr/store/main/getBestList.do?t_page=%EB%9E%AD%ED%82%B9&t_click=GNB&t_gnb_type=%EB%9E%AD%ED%82%B9&t_swiping_type=N'
driver.get(URL)

# print(len(oliveyoung_info))

oliveyoung_list = []

for i in range(30):
    oliveyoung_info = driver.find_elements(By.CSS_SELECTOR, 'div.prd_name > a')
    
    oliveyoung_info[i].click()
    time.sleep(2)

    brand = driver.find_element(By.CSS_SELECTOR, 'p.prd_brand').text
    # print(brand)
    name = driver.find_element(By.CSS_SELECTOR, 'p.prd_name').text
    price_1 = driver.find_element(By.CSS_SELECTOR, 'span.price-1 strike').text
    price_2 = driver.find_element(By.CSS_SELECTOR, 'span.price-2 strong').text
    review = driver. find_element(By.CSS_SELECTOR, 'div.prd_social_info b').text
    review_count = driver.find_element(By.CSS_SELECTOR, 'div.prd_social_info em').text

    oliveyoung_list.append([brand, name, price_1, price_2, review, review_count])

    driver.back()

# print(oliveyoung_list)

local_file_path = '/home/ubuntu/damf2/data/practice/oliveyoung'

def save_to_csv(oliveyoung_list):
    with open(local_file_path + 'oliveyoung-top-30', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(oliveyoung_list)

save_to_csv(oliveyoung_list)