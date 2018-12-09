
movie_person = ['alex','lucy','jack','sb_wupeiqi','linhaifeng']
movie_person1 = ['sb_lifei','david','lily']


ret = []
for p in movie_person:
    if  p.startswith('sb'):  # startswith 匹配相应字段的值
        ret.append(p)
print(ret)                  # 打印结果：['sb_wupeiqi']

# 对上面逻辑的优化改进(封装起来直接调用函数的逻辑)  以sb开头的值
def filter_test(array):
    res = []
    for y in array:
        if not y.startswith('sb'):
            res.append(y)
    return res
print(filter_test(movie_person))
# print(filter_test(movie_person1))

# 以 sb结果的值  用endswith函数

movie_person2 = ['tom','jim','roce_sb','game_sb']

# 可以写一个函数，如下：
def sb_show(name):
    return name.endswith('sb')

# lambda name:name.endswith('sb') 可以用此匿名函数完成




