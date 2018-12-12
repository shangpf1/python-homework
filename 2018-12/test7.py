# 内置函数

print(abs(-1))

print(all([1,3,5,7]))     # True 所有值的boolean为真，则为true
print(all([1,4,6,'']))    # false
print(all(''))           # 为空时也是true

print(any([1,'',0]))    # true 和all相反，只要有一个为真，则为真
print(any([0,'']))      # false

print(bin(3))           # 0b11


#  结果为 false
print(bool(''))
print(bool(None))
print(bool(0))

name = '你好'
print(bytes(name,encoding='utf-8'))  #编码 encode

print(bytes(name,encoding='utf-8').decode('utf-8'))  # 用什么方式编码就用什么方式解码  结果为：你好

print(bytes(name,encoding='gbk').decode('gbk'))  # 结果为：你好

# print(bytes(name,encoding='ascii'))  # ascii 不能编码中文

print(chr(46))     # 打印一个点

print(dir(all))


print(divmod(10,3))     #相除 取商拿余   结果为:（3,1)


# 将字典转换为字符串
dic = {'name':'alex'}
dic_str = str(dic)
print(dic_str)


print(bin(10))  # 10进制---》2进制
print(hex(12))  # 10进制---》16进制
print(oct(12))  # 10进制---》8进制


print(isinstance(1,int))
print(isinstance('abc',str))
print(isinstance([],list))
print(isinstance({},dict))
print(isinstance({1,4},set))


name = '哈哈哈哈啊'
print(globals())
print(__file__)         # .\test7.py

list = [1,2,100,-1,4]
print(max(list))
print(min(list))