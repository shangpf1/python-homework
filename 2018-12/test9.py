# map、reduce、filter函数的总结

l = [1,2,4,6]
print(list(map(str,l))) 
# 运行结果：['1', '2', '4', '6']


from functools import reduce
res = reduce(lambda x,y:x+y,l,3)
print(res)
# 运行结果：16

name = ['alex_sb','lifei']
resp = filter(lambda x:x.endswith('sb'),name)
print(list(resp))
# 运行结果：['alex_sb']

