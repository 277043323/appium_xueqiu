from time import sleep

from selenium.webdriver.common.by import By

from codejiang.basepage import Base


class GongGao(Base):
    def gonggao(self):
        self.swith(0)
        self.find(By.XPATH,'//*[@class="table-top"]').click()
        self.find(By.XPATH,'//*[@class="el-form demo-ruleForm"]/div[1]').send_keys("新增公告1")
        self.find(By.XPATH, '//*[@class="el-form demo-ruleForm"]/div[2]').send_keys("ann")
        self.find(By.XPATH, '//*[@class="el-form demo-ruleForm"]/div[3]').click()
        self.find(By.XPATH, '//*[@class="el-form demo-ruleForm"]/div[4]').click()


