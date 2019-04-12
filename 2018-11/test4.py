# from pymongo  import MongoClient  

# client = MongoClient('mogodb://39.107.96.138:27017/')

# print(client.database_names())

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('http://39.107.96.138:3000/')

# 点击登陆
driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[6]/a').click()

# 用户名 密码 登陆
driver.find_element_by_id('name').send_keys('user6')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_class_name('span-primary').click()

driver.find_element_by_class_name('span-success').click()
driver.find_element_by_id('tab-value').click()
driver.find_element_by_css_selector('#tab-value > option:nth-child(3)').click()

driver.find_element_by_id('title').send_keys('hello')

contentInput = driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll')

ActionChains(driver).move_to_element(contentInput).click().perform()

contentArea = driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre')
ActionChains(driver).move_to_element(contentArea).send_keys('恭喜你发帖成功！').perform()

driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input').click()



