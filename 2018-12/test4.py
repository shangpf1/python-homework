# reduce函数的应用

num1 = [1,2,5]

# sum = 0
# for num in num1:
#     sum+=num
# print(sum)


def reduce_test(array):
    sum = 0
    for num in array:
        sum+=num
    return sum
print(reduce_test(num1))

# 乘法
def mult_test(x,y):
    return x*y

# lambda x,y:x*y

# 终极版（加减乘除都可以用此函数方法）
def reduce_test(func,array):
    sum = array.pop(0)  #先将第一个数取出来  
    for num in array:
        sum=func(sum,num)
    return sum
print(reduce_test(lambda x,y:x*y,num1))
