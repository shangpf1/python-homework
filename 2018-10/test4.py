import unittest
import HTMLReport

class CnodeTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setUpClass-----")

    def setUp(self):
        print("this is setUp-----")

    def test_register(self):
        pass

    def test_login(self):
        pass

    def tearDown(self):
        print("this is tearDown-----")

    @classmethod
    def tearDownClass(self):
        print("tearDownClass----")
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(CnodeTest('test_register'))
    suite.addTest(CnodeTest('test_login'))
    return suite


if __name__ == '__main__':
    suite = suite()
    # 测试用例执行器
    runner = HTMLReport.TestRunner(report_file_name='test',  # 报告文件名，默认“test”
                                output_path='report',  # 保存文件夹名，默认“report”
                                verbosity=2,  # 控制台输出详细程度，默认 2
                                title='测试报告',  # 报告标题，默认“测试报告”
                                description='无测试描述',  # 报告描述，默认“无测试描述”
                                thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                # 是否按照套件添加(addTests)顺序执行，
                                sequential_execution=True
                                # 会等待一个addTests执行完成，再执行下一个，默认 False
                                )
    # 执行测试用例套件
    runner.run(suite)