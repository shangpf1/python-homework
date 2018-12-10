# reduce 函数的语法及实践

num_1 = [1,3,6,10]

def reduce_test(func,array,init=None):
    if init is None:
        res = array.pop(0)
    else:
        res = init
    for num in array:
        res = func(res,num)
    return res

print(reduce_test(lambda x,y:x/y,num_1))


# filter 将列表中所有的值筛选一遍重新得到一个新的列表，
# 而reduce 是将列表中所有的值压缩起来得到一个最终的结果

# reduce 函数

from functools import reduce
num = [2,5,10]
sum = reduce(lambda x,y:x*y,num)
print(sum)