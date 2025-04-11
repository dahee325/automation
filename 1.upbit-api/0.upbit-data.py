from datetime import datetime
import requests
import time
import csv

# 데이터 생성
upbit_url = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'

start_time = time.time()

bit_data_list = []

while time.time() - start_time < 60:
    res = requests.get(upbit_url)
    data = res.json()[0]

    bit_data = [
        data['market'],
        data['trade_date'],
        data['trade_time'],
        data['trade_price']
    ]
    bit_data_list.append(bit_data)
    time.sleep(10)

# 파일 생성
local_file_path = '/home/ubuntu/damf2/data/bitcoin/'

now = datetime.now()
file_name = now.strftime('%H-%M-%S') + '.csv'

# 파일 저장
with open(local_file_path + file_name, mode='w', newline='') as file: 
    # 내가 연 파일을 file에 저장, file은 with문에서만 살아있는 변수
    # mode='w' : write
    writer = csv.writer(file)
    writer.writerows(bit_data_list)