python_l =['spf','apple','pear','sun']
linux_l =['sun','pear','shy']

p_s = set(python_l)
l_s = set(linux_l)

print(p_s,l_s)    #分别打印出来

# 求交集
print(p_s.intersection(l_s))
print(p_s&l_s)

# 求并集
print(p_s.union(l_s))
print(p_s|l_s)

# 求差集
print(p_s-l_s)
print(l_s-p_s)

print(p_s.difference(l_s))
print(l_s.difference(p_s))
