from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
driver.get(URL)

# print(len(movie_info))

movie_list = []

for i in range(5):
    time.sleep(2)
    movie_info = driver.find_elements(By.CSS_SELECTOR, 'div.box-contents > a')
    # print(movie_info[i].get_attribute('innerHTML'))
    movie_info[i].click()
    time.sleep(2)

    title = driver.find_element(By.CSS_SELECTOR, 'div.title strong').text
    # print(title)
    director = driver.find_element(By.CSS_SELECTOR, 'div.spec > dl > dd:nth-child(2)').text
    # print(director)
    actors = driver.find_elements(By.CSS_SELECTOR, 'div.spec > dl > dd.on a')
    for actor in actors:
        actor.text
        # print(actor.text)

    movie_list.append([title, director])

    driver.back()