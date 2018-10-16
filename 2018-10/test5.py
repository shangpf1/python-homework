# 字符串的魔法2

# 判断是否是空格 空格，返回true ，不是返回false
y = " "
x = y.isspace()
print(x)

# 判断是否是标题
y1 = "this is a title"
x1 = y1.istitle()
print(x1)

x2 = y1.title()
print(x2)

x3 = y1.istitle()
print(x3)


# 将字符串中的每一个元素按照指定分隔符进行拼接
x4 = "你是风儿我是沙"
print(x4)

t = "_"   # t = " "
h = t.join(x4)
print(h)

# 全部变小写
x5 = "HiTr"
h1 = x5.lower()
print(h1)

# 处理大写的
x6 = x5.isupper()
print(x6)

x7 = x5.upper()
print(x7)


# 取出空白
x8 = "gtdfdurdf"
h2 = x8.lstrip()
h3 = x8.rstrip()
h4 = x8.strip()
h5 = x8.rstrip()
h6 = x8.rstrip("df")  #移除右侧的df字符
h7 = x8.lstrip("gt")  #移除左侧的df字符
print(h2)
print(h3)
print(h4)
print(h5)
print(h6)
print(h7)
