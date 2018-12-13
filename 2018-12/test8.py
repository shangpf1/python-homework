# max 函数和 min函数的实践

# zip 方法 数据必须是可迭代类型

# 字典 元组 字符串 都是序列

p = {'name':'alex','age':18,'sex':'男'}
print(zip(p.keys(),p.values()))            # 打印结果：<zip object at 0x000001C4D5290A48>  为内存地址
print(list(zip(p.keys(),p.values())))      # 打印结果：[('name', 'alex'), ('age', 18), ('sex', '男')]

# max 方法
age_dict = {'alex_age':18,'wuxue_age2':100,'lijing_age3':30,'wangzhao_age4':40}
print(max(age_dict.values()))    # 结果为：100
print(max(age_dict))            # 结果为： wuxue_age2


print(max(zip(age_dict.values(),age_dict.keys())))    # 结果为：(100, 'wuxue_age2')

people = [
    {'name':'alex','age':100},
    {'name':'jack','age':80},
    {'name':'lucy','age':20}
]
print(max(people,key = lambda dic:dic['age']))      # 结果为：{'name': 'alex', 'age': 100}

ret = []
for item in people:
    ret.append(item['age'])
print(ret)

for item in  zip(age_dict.values(),age_dict.keys()):
    print('----------',item)

    # print(list(max(zip(age_dict.values(),age_dict.keys()))))        # 结果为：[100, 'wuxue_age2']