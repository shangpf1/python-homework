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