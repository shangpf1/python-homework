
l = [1,2,4,6]
print(list(map(str,l)))


from functools import reduce
res = reduce(lambda x,y:x+y,l,3)
print(res)

name = ['alex_sb','lifei']

resp = filter(lambda x:x.endswith('sb'),name)
print(list(resp))

