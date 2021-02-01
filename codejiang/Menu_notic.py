from time import sleep

from selenium.webdriver.common.by import By

from codejiang.basepage import Base


class GongGao(Base):
    def gonggao(self):
        sleep(5)
        self.find(By.XPATH,'//*[@class="table-top"]/button').click()
        sleep(3)
        # self.find(By.XPATH,'//*[@class="el-form demo-ruleForm"]/div[1]/input').send_keys("新增公告1")

        self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(1) input').send_keys("新增公告1")
        # self.find(By.XPATH, '//*[@class="el-form demo-ruleForm"]/div[2]/input').send_keys("ann")
        self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(2) input').send_keys("ann")
        self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(3) input').click()
        # self.find(By.XPATH, '//*[@class="el-form demo-ruleForm"]/div[4]/input').click()
        self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(1) input').click()
        #这个函数没有生效，很是奇怪
        self.forward()


