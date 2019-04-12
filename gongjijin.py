# 有关图形验证码，且验证码中的数字必须是不同的颜色才可
# 此次用的时百度ocr的图形验证码方法，并不是全能的，

import requests,base64
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://person.shgjj.com/gjjweb/#/login5/A0')
time.sleep(2)

# 验证码
image_ele = driver.find_element_by_xpath('//*[@id="mobilephone"]/form/div[2]/div[1]/input')

image_ele.screenshot('./image.png')

# https://console.bce.baidu.com/ai/?fromai=1#/ai/imagerecognition/overview/index 百度ocr
# client_id 为官网获取的AK， client_secret 为官网获取的SK   https://console.bce.baidu.com/ai/?fromai=1#/ai/imagerecognition/app/list
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vqZCFY4jFqbIUWVKn7P2ZGCE&client_secret=cjTrCqVqIo5XzkzkNpucrkh8dSF8Bjnf'
res = requests.get(host)
r = res.json()
print(r)

access_token = r['access_token']
print(access_token)

# access_token = '#####调用鉴权接口获取的token#####'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'./image.png', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
imageres = requests.post(url,data=params)
image_json = imageres.json()
print(imageres.json())

image_num = image_json['words_result'][0]['words']
driver.find_element_by_id('imagecodel').send_keys(image_num)