# filter函数（过滤函数）实践02

# 以 sb结束的值  用endswith函数

# 可以写一个函数，如下：
def sb_show(name):
    return name.endswith('sb')

# lambda name:name.endswith('sb') 可以用此匿名函数完成

# 终极版
movie_person2 = ['tom','jim','roce_sb','game_sb']

def filter_test(func,array):
    res = []
    for y in array:
        if not func(y):
            res.append(y)
    return res
reponse = filter_test(lambda n:n.endswith('sb'),movie_person2)
print(reponse)


# filter 函数
movie_person3 = ['shu_sb','yen_sb','sb_hsi','hsb','shidf']

print(filter(lambda n:not n.endswith('sb'),movie_person3))

reponse1 = filter(lambda n:not n.endswith('sb'),movie_person3)
print(list(reponse1))  #结果中过滤掉以sb结尾的值


