# 集合是一个无序的，不重复的数据组合，它的主要作用如下：

# 去重，把一个列表变成集合，就自动去重了
# 关系测试，测试两组数据之前的交集、差集、并集等关系
# 集合(set)：把不同的元素组成一起形成集合，是python基本的数据类型。

# 集合元素(set elements):组成集合的成员(不可重复)

# 创建列表的2种方式
a = [1,3,6]
b= list([5,7,9])
print(a)
print(b)


# set ：去重
s = set('alex li')
print(s)     #打印结果：{'e', ' ', 'i', 'l', 'x', 'a'}

s1 = ['ahd','ert','ahd']
s2 = set(s1)
print(s2,type(s2))  #结果及数据类型 {'ahd', 'ert'} <class 'set'>

# 可以将上面的结果转换为列表
s = list(s2)
print(s,type(s))  #打印结果：['ahd', 'ert'] <class 'list'>


# 集合对象是一组无序排列的可哈希的值：集合成员可以做字典的键　
li=[[1,2],'a','b']    #每个元素必须是不可变的，即不可哈希，除了 字典 、元组
s =set(li) #TypeError: unhashable type: 'list'
print(s)
# 如果将上面的改为 li=[2,'a','b']



