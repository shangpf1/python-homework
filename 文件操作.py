# 文件处理的3步操作（打开、读取及关闭）
# 切记：下面的慕容飞儿文件必须与此文件在同级目录下

# 打开文件
f = open('慕容飞儿',encoding='utf-8')
# data = f.read()
# print(data)
# f.close()   #打开之后必须要关闭文件，不然会不停的占系统内存

# readline用法

# data = f.readline()
# print('第一次打印：',data)
# print('第二次打印：',data)
# print('第三次打印：',data)

# readlines用法
data = f.readlines()
print('第一次打印：',data)
print('第二次打印：',data)