# 列表的魔法一

li = [1,2,3,5,'56f','er','王三']

# 进行修改
li[2] = 100
print(li)

# 通过切片进行修改
li[1:3] = [80,500]
print(li)

# in的操作
y = '李飞' in li
print(y)

# 列表转换为字符串时：需要写for循环一个一个处理，（列表中既有数字也有字符串）
li1 = [1,3,6,'df','57',9,'56j']

s = ''
for i in li1:
    s = s + str(i)
print(s)

# 直接使用join方法，（列表中只有字符串）
li2 = ['3g','dgy','45']
y1 = ''.join(li2)
print(y1)

# 原来的列表后加
li3 = [2,4,'oj']
li3.append(6)
print(li3)

# 清空列表
li3.clear()
print(li3)

# 拷贝，浅拷贝
li4 = li2.copy()
print(li4)

# 计算元素出现的次数
li5 =li2.count('3g')
print(li5)

li4.extend('ty')
print(li4)

# 根据值获取当前值索引位置（左边优先）
li6 = [4,6,'fy']
h = li6.index('fy')
h1 = li6.index(6)
print(h)
print(h1)

# 在列表的前面插入值(指定索引位置，进行插入值)
li6.insert(0,'ly')
print(li6)

# 默认删除列表中的最后一个值
li7 = [4,5,7,0,2]
f= li7.pop()
print(li7)
print(f)     # 删除的具体值

# 删除列表中的指定值
li8 = [6,7,'g',0]
li8.remove('g')
print(li8)

# 将当前列表进行反转
li9 = [3,5,8,1,0]
li9.reverse()
print(li9)

# 进行排序
li9 = [3,5,8,1,0]
# li9.sort()            #正序
li9.sort(reverse=True)  # 倒序
print(li9)



