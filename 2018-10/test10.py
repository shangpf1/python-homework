# 字典的魔法

dict = {1:'shg','name':'lucy','Age':19}
y = dict['name']

#删除某个键值对
del dict['name']

print(dict)
print(y)

for item in dict:
    print(item)

for item in dict:
    print(item,dict[item])

# 根据序列创建字典，并指定统一的值
v = dict.fromkeys(['234','frt'],123)
print(v)


# 根据key获取值，key不存在时，可以指定默认值
v1 = dict.get('k1')
print(v1)

v2 = dict.get('k2',344)
print(v2)

dict1 = {6:'123','age':12,'class':6}
v3 = dict1.pop('class')
print(v3)

# 更新的2中方法
dict1.update({'age':90,'sex':'男'})
print(dict1)

dict1.update(age='70',name='lucy')
print(dict1)

