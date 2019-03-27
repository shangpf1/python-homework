import unittest
# from A_UnitTest_basicDemo_ok.function import *

# 定义一个加法的函数
def add(x,y):
    return x+y

# 定义一个减法函数
def minus(x,y):
    return x-y

# 定义一个乘法函数
def multi(x,y):
    return x*y

# 定义一个除法函数
def divide(x,y):
    return x/y

class TestFunc(unittest.TestCase):
    # 继承自unittest.TestCase
    # 重写TestCase的setUp()、tearDown()方法：在每个测试方法执行前以及执行后各执行一次
    def setUp(self):
        print("do something before test : prepare environment")

    def tearDown(self):
        print("do something after test : clean up ")
    
    # 测试方法均已test开头，否则是不被unittest识别的
    def test_add(self):
        print("add:")
        self.assertEqual(3,add(1,2))

    # @unittest.skip("i don't want to run this case -> test_minus() ... ")
    def test_minus(self):
        print("minus")
        self.assertEqual(3,minus(5,2))

    def test_multi(self):
        print("multi")
        self.assertEqual(6,multi(2 ,3))

    def test_divide(self):
        self.skipTest('do not run  test_divide()')
        print("divide")
        self.assertEqual(2,divide(4,2))
        

if __name__ == "__main__":
    suite = unittest.TestSuite()
# 定义list，按照list里的顺序执行测试用例
tests=[TestFunc("test_add"),TestFunc("test_minus"),TestFunc("test_multi"),TestFunc("test_divide")]
suite.addTests(tests)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# 运行结果如下：
test_add (__main__.TestFunc) ... do something before test : prepare environment
add:
do something after test : clean up
ok
test_minus (__main__.TestFunc) ... do something before test : prepare environment
minus
do something after test : clean up
ok
test_multi (__main__.TestFunc) ... do something before test : prepare environment
multi
do something after test : clean up
ok
test_divide (__main__.TestFunc) ... do something before test : prepare environment
do something after test : clean up
skipped 'do not run  test_divide()'

----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK (skipped=1)