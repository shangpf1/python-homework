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

