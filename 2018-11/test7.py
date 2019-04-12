
# def foo(n):
#     print(n)

# def bar(name):
#     print('my name is %s'%name)

# foo(bar)
# foo(bar('lucy'))

from pymongo import MongoClient

client = MongoClient('mongodb://118.31.19.120:27017/')
print(client.database_names())