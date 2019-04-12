# 打开百度页面相关图片的上传及截图

from selenium import webdriver
from os import path


d = path.dirname(__file__)
index = path.join(d,'index.png')
image = path.join(d,'image.png')
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
driver.save_screenshot('./index.png')

driver.find_element_by_class_name('soutu-btn').click()
driver.save_screenshot('./image.png')

# 点击本地上传按钮，后面的路径是windows中的路径格式
driver.find_element_by_class_name('upload-pic').send_keys('C:\\Users\\shangpengfei\\Desktop\\Penguins.jpg')
