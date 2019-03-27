# zip方法（有点像拉链，一一对应的）

#打印结果：<zip object at 0x000002A5818D0BC8>
print(zip(('a','b','c'),('1','2','4')))   

# 运行结果：[('a', '1'), ('b', '2'), ('c', '4')]
print(list(zip(('a','b','c'),('1','2','4'))))


# 下面2条运行结果一样，必须是一一对应：[('a', '1'), ('b', '2'), ('c', '4')]
print(list(zip(('a','b','c'),('1','2','4','8'))))

print(list(zip(('a','b','c','f'),('1','2','4'))))


# 运行结果：[('name', 'luly'), ('age', 18), ('sex', 'girl')]
p = {'name':'luly','age':18,'sex':'girl'}
print(list(zip(p.keys(),p.values())))

# 运行结果：['name', 'age', 'sex']
print(list(p.keys()))

# 运行结果：['luly', 18, 'girl']
print(list(p.values()))

# 运行结果：[('a', '1'), ('b', '2'), ('c', '3'), ('f', '4')]
print(list(zip('abcf','1234')))


