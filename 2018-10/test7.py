# 字符串的魔法三

# 包含字母为真，别的为假
x = "dfdgfgh我的"
y = x.isalpha()
print(y)

# 判断是否为数字，下面的功能比较强大
x1 = "23455"
y1 = x1.isdecimal()
y2 = x1.isdigit()
h = x1.isnumeric()
print(y1,y2,h)

# 字母、数字、下划线：标识符 def class  返回true
x2 = "_shsidfds"
x3 = "fg2_333"
x4 = "def"
y3 = x2.isidentifier()
y4 = x3.isidentifier()
y5 = x4.isidentifier()
print(y3,y4,y5)

# 将字符串进行分割成3份,且包含分割的字符
r = "dsfdkftgfghkghjhjuytyre"
g = r.partition('k')  # 从前面分割成3份
g1 = r.rpartition('k') #从后面分割成3份
print(g,g1)


# 将字符串进行分割成3份,且不包含分割的字符
g2 = r.split("k")
g3 = r.rsplit('k')
print(g2,g3)

# 控制 \n  \t 
r1 = "fgfhgjhgkjkrtuytuf556yi"
g4 = r1.isprintable()
g5 = r1.endswith('i')   # 以字符结尾
g8 = r1.startswith('f')  # 以字符开头
print(g4,g5,g8)

# 分割，只能根据 true false来判断是否保留换行
r2 = "fdfgfhgf\nfgfjhetret\nseqfrgdr\noqwrtyy"
g6 = r2.splitlines(True)   # 保留换行
g7 = r2.splitlines(False)  #不保留换行
print(g6)
print(g7)

# 大小写转换
r3 = "shsYhiTDHD"
z = r3.swapcase()
print(z)


