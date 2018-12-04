# 有关匿名函数的用法

def calc(x):
    return x+1

res = calc(10)
print(res)

# 匿名函数
y = lambda x : x + 1  #形参：返回值
print(y(110))


p = lambda x,y,z:(x+1,y+1,z+1)
print(p(1,2,3))

# 运行结果：name_sb 有如下2种方法：

def change_name(name):
    return name + '_sb'
e = change_name('name')
print(e)

res1 = lambda x:x+'_sb'
funct = res1('name')
print('匿名函数的运行结果：',funct)

