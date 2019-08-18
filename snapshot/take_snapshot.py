import requests
import os
from datetime import datetime

# url for capturing snapshots

api_url = "https://urlscan.io/liveshot/"
capture_url = "https://www.medium.com/"
height = "6000"
width = "2048"

params = {"width": width, "height": height, "url":capture_url}

res = requests.get(api_url, params= params)

# print(res.status_code)

if not os.path.exists('data/'):
	os.mkdir("data/")

image_file_path = "data/medium_" + datetime.strftime(datetime.now(),'%Y_%m_%d') + ".png"
# print(image_file_path)

with open(image_file_path,'wb') as f:
	# f.write(res.text.encode('utf-8'))
	f.write(res.content)

print("taken snap for today") 