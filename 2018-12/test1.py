# 匿名函数的应用及实践

# 方法一：
def foo(x):
    return x+1
y= foo(5)
print(y)   #结果：6

# 方法二：
y = lambda x:x+1
print(y(5))   #结果：6


# 求此列表中数的平方
num = [1,3,6,9,6,7]

res = []
for i in num:
    res.append(i**2)

print(res)  #结果：[1, 9, 36, 81, 36, 49]


# 定义一个方法，直接调用此方法
def map_test(array):
    res = []
    for i in array:
        res.append(i**2)
    return res

res = map_test(num)

print(res)    #结果：[1, 9, 36, 81, 36, 49]


num1 = [2,4,6,8,9,0]
#  def lambda x:x+1 自增1的函数
def add_one(x):
    return x+1   #结果：[3, 5, 7, 9, 10, 1]

# def lambda x:x-1  自减1的函数
def reduce_one(x):
    return x-1  #结果：[1, 3, 5, 7, 8, -1]

# 将下面的逻辑封装到此函数中
def map_test1(func,array):
    res = []
    for i in array:
        yt = func(i)  # add_one(i)
        res.append(yt)
    return res

# 函数自增1的结果
print(map_test1(add_one,num1))
# print(map_test1(lambda x:x+1,num1))

# 函数自减1的结果
print(map_test1(reduce_one,num1))
# print(map_test1(lambda x:x-1,num1))

# 函数的平方的结果 [4, 16, 36, 64, 81, 0]
print(map_test1(lambda x:x**2,num1))    


