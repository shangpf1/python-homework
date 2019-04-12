# 用爬虫抓取页面信息后并且将结果保存到表格中

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

# 运行结果如下：
DevTools listening on ws://127.0.0.1:56799/devtools/browser/6bf2e521-389c-42fc-8bb8-501a74e89572
【Python之父再度发声：我们能为中国的“996”程序员做什么？】日前，Python之父再度为"中国程序员996工作制"发声，他在Python上发帖表示，一周前一些中国程序员创建了996.icu抱怨恶劣
的工作条件，现在该网站已被各种中国浏览器禁止访问，我们怎么样才能帮助中国开发者？对此，CPython核心开发人员Sent 展开全文c 电脑报 04月08日 09:34 来自 微博 weibo.com 04月08日
09:34 来自 微博 weibo.com 收藏 转发 12289 评论 2283 4939
【Python之父发声：我们能为中国的“996”程序员做什么？】日前，GitHub上个“996.ICU”项目控诉“996”工作制的不人道引发全球关注，对此Python之父吉多·范罗苏姆认为996工作制是不
人道的，呼吁媒体和政府积极关注这一事件……详情点击：OPython之父发声：我们能为中国的“996”程序员做什么？ IT之家 04月08日 07:23 来自 IT之家 04月08日 07:23 来自 IT之家 收藏
转发 130 评论 87 143
【视频丨996工作制惹争议，Python之父发声：我们能为中国的程序员做什么？】4月8日，P计算机程序设计语言之父为"中国程序员996工作制"发声，另一位开发者提出的建议是：让大家都意识到
这是一种劳动“剥削”，列出所有执行996工作制的公司，拒绝与它们合作。O视频丨996工作制惹争议，Python之父发声：我们能为中国的程序员做什么？ 21世纪经济报道 04月08日 20:16 来自
21财经 04月08日 20:16 来自 21财经 收藏 转发 48 评论 74
