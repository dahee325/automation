from selenium import webdriver
from selenium.webdriver.common.by import By
import time # 강제로 시간을 멈추기 위해서
import csv

driver = webdriver.Chrome()

URL = 'https://www.melon.com/chart/index.htm'
driver.get(URL)

# a태그에 클래스가 btn.song_info 인 결과들 가져옴
# find_element() : 조건에 맞는 요소를 하나만 찾음
# find_elements() : 조건에 맞는 요소를 모두 찾음
song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.song_info')
# print(len(song_info)) # => 전체 데이터가 들어있음

song_list = []

for i in range(2):
    song_info[i].click()
    time.sleep(2) # 2초

    # 제목 하나만 찾기
    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    # span태그가 여러개지만 find_element()를 사용했기 때문에 첫번쨰 요소만 출력
    artist = driver.find_element(By.CSS_SELECTOR, 'div.artist span').text # div.artist > a > span (>는 직계) = div.artist span (공백은 후손)
    # 여러개를 찾은 다음 인덱스 접근
    meta_data = driver.find_elements(By.CSS_SELECTOR, 'div.meta dd') ## div.meta에서 dd태그를 모두 출력
    # print(meta_data[1].text)

    # 발매일 정보를 특정
    publish_date = driver.find_element(By.CSS_SELECTOR, 'dl.list > dd:nth-of-type(2)').text
    # 좋아요 수 출력
    like_cnt = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    like_cnt = like_cnt.replace(',', '') # 쉼표 지우기

    song_list.append([title, artist, publish_date, like_cnt])

    driver.back()

local_file_path = '/home/ubuntu/damf2/data/melon/'

# csv파일로 저장
def save_to_csv(song_list):
    with open(local_file_path + 'melon-top-100.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(song_list) # 여러줄을 동시에 csv로 바꿔줌

save_to_csv(song_list)
