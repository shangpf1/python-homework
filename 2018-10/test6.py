# 运算符的用法

# in 的使用，下面name 这个字符串中有3个字符

name = '尚鹏飞'

# 尚、鹏、飞 、尚鹏、鹏飞 其中任意一个在name中就打印ok
if '尚' in name:   
    print('ok')
else:
    print('Error')

# not in 的使用
if '飞' not in name:
    print('1')
else:
    print('2')
