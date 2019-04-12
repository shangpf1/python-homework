def test_add(self):
        
        self.assertEqual(3,add(1,2))


# 将下面的逻辑封装到此函数中

num1 = [2,4,6,8,9,0]
def map_test1(func,array):
    res = []
    for i in array:
        yt = func(i)  # add_one(i)
        res.append(yt)
    return res

# 函数自增1的结果
# print(map_test1(add_one,num1))
print(map_test1(lambda x:x+1,num1))

# 函数自减1的结果
# print(map_test1(reduce_one,num1))
print(map_test1(lambda x:x-1,num1))

# 函数的平方的结果 [4, 16, 36, 64, 81, 0]
print(map_test1(lambda x:x**2,num1))  