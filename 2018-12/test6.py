# 总结 filter reduce map函数的用法

# 处理序列中的每个元素，得到的结果是一个“列表”，该列表元素个数及位置与原来一样
# map()

# filter 遍历序列中的每个元素，判断每个元素得到布尔值，如果是True则留下来

people = [
    {'name':'alex','age':1000},
    {'name':'lucy','age':10000},
    {'name':'jack','age':9000},
    {'name':'rose','age':18}
]

# 过滤掉people中年龄大于18的人  -- filter函数
res = filter(lambda p:p['age']<=18,people)
print(list(res))


# reduce 函数的用法
from functools import reduce

print(reduce(lambda x,y:x+y,range(5),1))
print(reduce(lambda x,y:x+y,range(1,5)))


# map函数的用法
num = [1,3,5,7]
def map_test(func,array):
    resp = []
    for i in array:
        yt = func(i)
        resp.append(yt)
    return resp
print(map_test(lambda x:x**2,num))
print(map_test(lambda x:x+1,num))
print(map_test(lambda y:y-1,num))
    