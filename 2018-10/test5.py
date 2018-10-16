# 字符串的魔法

# capitalize 首字母大写
test4 = "aLex"
f = test4.capitalize()
print(f)

# 所有字母都变小写，casefold 更牛些
f1 = test4.casefold()
print(f1)

f2 = test4.lower()
print(f2)

# 居中，10是指长度，* 是指2边的填充，不过这里可以不用写（方法中的参数中无等号必须写，没的话可以不用写）
f3 = test4.center(10,'*')
print(f3)

f6 = test4.ljust(10,"*")   # 左边
print(f6)

f7 = test4.rjust(10,"*")   # 右边
print(f7)

# endswith 以啥字符结尾
f4 = test4.endswith("h")
f5 = test4.startswith("df")  # 以啥开始
print(f4)
print(f5)

# find 的用法
test= "aleryer"
r = test.find("er")
# r = test.find("er",5,8)
print(r)

# 格式化，将一个字符串中的占位符替换为指定的值
test1 = 'i am {name}'
print(test1)
y = test1.format(name='jame')
print(y)

test2 = 'i am {name},age {a}'
# y1 = test2.format_map(name='lucy',a=19)
y2 = test2.format_map({"name":'lucy',"a":19})
print(y2)

# isalnum方法 ，必须是字母或数字，数字和字母
test3 = "sunshine09"
y3 = test3.isalnum()
print(y3)



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
