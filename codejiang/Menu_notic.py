from time import sleep

from selenium.webdriver.common.by import By

from codejiang.basepage import Base
import allure


@allure.feature("公告栏page")
class GongGao(Base):
    @allure.story("新增公告成功")
    def gonggao(self):
        locator = (By.XPATH,'//*[@class="table-top"]/button')
        self.wait_time(locator)
        self.find(By.XPATH,'//*[@class="table-top"]/button').click()
        # sleep(3)  #这里使用强制等待，等待3s
        # self.find(By.XPATH,'//*[@class="el-form demo-ruleForm"]/div[1]/input').send_keys("新增公告1")
        with allure.step("点击公告标题"):
            self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(1) input').send_keys("新增公告1")
        # self.find(By.XPATH, '//*[@class="el-form demo-ruleForm"]/div[2]/input').send_keys("ann")
        with allure.step("点击公告作者"):
            self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(2) input').send_keys("ann")
        with allure.step("点击公告展示期"):
            self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(3) input').click()
        with allure.step("选中一个开始展示时间"):
            self.find(By.XPATH,'//*[@class="el-date-table"]//tr[2]/td[3]/div').click()
        with allure.step("确定选中的开始时间"):
            self.find(By.XPATH,'//*[@class="el-picker-panel__footer"]/button[2]').click()
        with allure.step("选中一个结束时间"):
            self.find(By.CSS_SELECTOR,'.el-date-table tr:nth-child(2)>td:nth-child(3)>div>span').click()
        with allure.step("确定结束的时间"):
            self.find(By.CSS_SELECTOR,'.el-picker-panel__footer>button:nth-child(2)>span').click()
        # self.find(By.XPATH, '//*[@class="el-form demo-ruleForm"]/div[4]/input').click()
        with allure.step("编辑公告内容"):
            self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(1) input').click()
        #这个函数没有生效，很是奇怪
        self.forward()


