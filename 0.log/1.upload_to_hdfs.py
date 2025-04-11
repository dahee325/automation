from hdfs import InsecureClient
import os # 운영체제를 컨트롤하는 라이브러리

client = InsecureClient('http://localhost:9870', user='ubuntu')

# client.makedirs('/input/logs') # input폴더 안에 logs폴더 생성

local_file_path = '/home/ubuntu/damf2/data/logs/'
hdfs_file_path = '/input/logs/'

local_files = os.listdir(local_file_path)

for file_name in local_files:
    if not client.content(hdfs_file_path + file_name, strict=False): # 데이터가 없으면 업로드
        client.upload(hdfs_file_path + file_name, local_file_path + file_name)
