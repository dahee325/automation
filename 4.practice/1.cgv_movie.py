from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

URL = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
driver.get(URL)

# print(len(movie_info))

movie_list = []

for i in range(10):
    time.sleep(2)
    movie_info = driver.find_elements(By.CSS_SELECTOR, 'div.box-contents > a')
    # print(movie_info[i].get_attribute('innerHTML'))
    movie_info[i].click()
    time.sleep(2)

    title = driver.find_element(By.CSS_SELECTOR, 'div.title strong').text
    # print(title)
    director = driver.find_element(By.CSS_SELECTOR, 'div.spec > dl > dd:nth-child(2)').text
    # print(director)
    
    actor_list = []
    actors = driver.find_elements(By.CSS_SELECTOR, 'div.spec > dl > dd.on a')
    for actor in actors:
        actor.text
        actor_list.append(actor.text)
        # print(actor.text)
    
    genre = driver.find_element(By.CSS_SELECTOR, 'div.spec dt:nth-of-type(3)').text
    # print(genre)
    opening_date = driver.find_element(By.CSS_SELECTOR, 'div.spec dd:nth-of-type(6)').text
    # print(opening_date)

    movie_list.append([title, director, actor_list, genre, opening_date])

    driver.back()

# print(movie_list)

local_file_path = '/home/ubuntu/damf2/data/cgv_movie/'

def save_to_csv(movie_list):
    with open(local_file_path + 'cgv-top-10', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(movie_list)

save_to_csv(movie_list)