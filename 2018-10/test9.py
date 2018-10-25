# 元组的魔法一

# 不可修改、增加、删除，但是可以切片和列表一样也可切片

tuple1 = (1,2,4,5,)
print(tuple1)

# 索引
v = tuple1[0]
print(v)

# 元组可转换成列表
list1 = list(tuple1)
print(list1)

# 元组中必须是字符，从可以用join
tuple2 = ('df','fgf','hjh')
y = "_".join(tuple2)
print(y)

# 循环、迭代
for item in tuple1:
    print(item)

# 
tuple3 = (22,'dfg',(11,45),[(67,90)],True,3,9,)
v = tuple3[3][0][0]
print(v)      # 打印结果：67