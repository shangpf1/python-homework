
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


# 元素定位的八种方法 

# driver.find_element_by_id('kw').send_keys('helloworld')
# driver.find_element_by_name('wd').send_keys('helloworld')
# driver.find_element_by_class_name('s_ipt').send_keys('helloworld')
# driver.find_element_by_css_selector('#kw').send_keys('helloworld')
# driver.find_element_by_link_text('新闻').click()
# driver.find_element_by_partial_link_text('新').click()
# driver.find_element_by_tag_name()    此方法基本不用了！！！
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('helloworld')

# eles = driver.find_elements_by_class_name('mnav')
eles = driver.find_elements_by_css_selector('#u1')
print(len(eles))

for ele in eles:
    print('txt:',ele.text)

# 运行结果如下：
1
txt: 新闻
hao123
地图
视频
贴吧
学术
登录
设置
更多产品