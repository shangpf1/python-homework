# 用爬虫抓取页面信息后并且将结果中的数据保存到表格中

from selenium import webdriver
# import time
import xlwt   #写入表格
driver = webdriver.Chrome()

driver.get('https://s.weibo.com/')

driver.maximize_window()

keyword = 'python之父'
driver.find_element_by_css_selector('div[class="search-input"]>input[type="text"]').send_keys(keyword)
driver.find_element_by_class_name('s-btn-b').click()

# driver.implicitly_wait(10)  隐性等待
eles = driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')

# 新建一个表格
wb = xlwt.Workbook()
wt = wb.add_sheet(keyword)

# 第一行每列的数据
wt.write(0,0,'标题')
wt.write(0,1,'发送人')
wt.write(0,2,'发布时间')
wt.write(0,3,'来源')
wt.write(0,4,'收藏数')
wt.write(0,5,'转发')
wt.write(0,6,'评论')
wt.write(0,7,'点赞')

counter = 0
for ele in eles:
    counter+=1
    title = ele.find_element_by_css_selector('p[class="txt"]').text
    username = ele.find_element_by_css_selector('a[class="name"]').text
    time = ele.find_element_by_css_selector('p[class="from"]').text
    source= ele.find_element_by_css_selector('p[class="from"]').text
    coll = ele.find_element_by_link_text('收藏').text
    coll_num =coll.split('收藏')[1]
    
    forward = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(2)').text
    forward_num =forward.split('转发')[1]
    comment = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(3)').text
    comment_num = comment.split('评论')[1]
    like = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(4)').text
    print(title,username,time,source,coll,forward,comment,like)
    
    wt.write(counter,0,title)
    wt.write(counter,1,username)
    wt.write(counter,2,time)
    wt.write(counter,3,source)
    wt.write(counter,4,coll_num)
    wt.write(counter,5,forward_num)
    wt.write(counter,6,comment_num)
    wt.write(counter,7,like)

wb.save('webo.xls')
driver.quit()