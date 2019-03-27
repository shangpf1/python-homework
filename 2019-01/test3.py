# 打开百度首页并且保存截图

from selenium import webdriver
# import time
from os import path


# d = path.dirname(__file__)
# index = path.join(d,'index.png')
# hao123 = path.join(d,'hao123.png')

driver = webdriver.Chrome()


driver.get('https://www.baidu.com/')

driver.maximize_window()

driver.find_element_by_link_text('hao123').click()
# time.sleep(3000)
driver.save_screenshot('./hao123.png')

driver.back()
driver.save_screenshot('./index.png')
