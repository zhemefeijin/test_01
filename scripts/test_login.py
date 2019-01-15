import unittest
import allure

class Test_login(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_username(self):
        allure.attach('描述','这也是用户名的测试脚本')
        print('mima')
        assert 1

    @allure.step(title='密码的测试脚本')
    def test_password(self):
        print('hello python')
        assert False

    @allure.step(title='登陆的测试脚本')
    def test_login(self):
        print('123')
        assert True
    @allure.step(title='第一次添加脚本内容')
    def test_sub(self):
        print('you are beautifug girl')
        assert 1