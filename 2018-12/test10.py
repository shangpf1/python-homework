# 迭代和递归    迭代：每次的结果都回依赖上次的结果（如：有爸爸才有儿子）,更新换代的过程
# 递归：如：问路，一个问一个，最后问到知道路的那个人
# 生成器：可理解为一种数据类型，自动实现迭代器协议  ，是可迭代对象

l = [1,3,'gy']
for i in l:
    print(i)

# iter = l.__iter__()     #遵循迭代器协议，生成可迭代对象
# print(iter.__next__())

index = 0
while  index < len(l):
    print(l[index])
    index+=1     #打印结果：gy

def test():
    yield 1
g = test()
print(g)        #generator object 生成器对象
print(g.__next__())    #打印结果：1

# 三元表达式

name = 'alex'
# nmae = 'lifei'
res = 'SB' if name == 'alex' else '帅哥'
print(res)            #打印结果：SB


# 列表解析
egg_list = []
for i in range(10):
    egg_list.append('鸡蛋%s' %i)
print(egg_list)      #打印结果：['鸡蛋0', '鸡蛋1', '鸡蛋2', '鸡蛋3', '鸡蛋4', '鸡蛋5', '鸡蛋6', '鸡蛋7', '鸡蛋8', '鸡蛋9']

l = ['鸡蛋%s' %i  for i in range(10)]
print(l)             #打印结果：['鸡蛋0', '鸡蛋1', '鸡蛋2', '鸡蛋3', '鸡蛋4', '鸡蛋5', '鸡蛋6', '鸡蛋7', '鸡蛋8', '鸡蛋9']

ll = ['鸡蛋%s' %i  for i in range(10) if i > 5]
print(ll)            #打印结果：['鸡蛋6', '鸡蛋7', '鸡蛋8', '鸡蛋9']


laomuji = ('鸡蛋%s' %i  for i in range(10))     #生成器表达式
print(laomuji)

print(next(laomuji))     # print(laomuji.__next__())
print(next(laomuji)) 
print(next(laomuji)) 
print(next(laomuji)) 
print(next(laomuji)) 
print(next(laomuji)) 
print(next(laomuji)) 
print(next(laomuji)) 
print(next(laomuji)) 
print(next(laomuji)) 

