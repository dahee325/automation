from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

URL = 'https://comic.naver.com/webtoon?tab=mon'
driver.get(URL)

webtoon_info = driver.find_elements(By.CSS_SELECTOR, 'a.ContentTitle__title_area--x24vt')
print(len(webtoon_info))

# webtoon_list = []

# for i in range(5):
#     webtoon_info[i].click()
#     time.sleep(2)

    # title = driver.find_element(By.CSS_SELECTOR, 'div.EpisodeListInfo__info_area--hkinm').text
    # writer = driver.find_element(By.CSS_SELECTOR, 'div.EpisodeListInfo__comic_info--yRAu0').text
    # print(title)

    # webtoon_list.append([title, writer])

    # driver.back()
# print(webtoon_list)