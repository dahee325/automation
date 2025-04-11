import requests
from bs4 import BeautifulSoup

lotto_url = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(lotto_url)

soup = BeautifulSoup(res.text, 'html.parser') # 파싱

balls = soup.select('span.ball_645') # sapn태그를 갖고있고 클래스가 ball_645인 데이터 출력
for ball in balls:
    print(ball.text) # 숫자만 출력