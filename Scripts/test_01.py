import allure
class Test_Page():

    @allure.step(title="这是第一次测试的测试步骤")
    def test_j_01(self):
        print("haha")
        assert True

    @allure.step(title="这是第二次测试的测试步骤")
    def test_j_02(self):
        print("hello")
        assert False