import selenium
import selenium.webdriver
import time

import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from codejiang.basepage import Base
from codejiang.common.data import Datas
from codejiang.fengzhuang import Fengzhuang
from codejiang.index009 import Shouye

class Main(Base):
    def goto_shouye(self):
        #
        # Fengzhuang().get_url("https://tea.codejiang.com/login")
        # Fengzhuang().findelement().send_keys('guohongxia')
        # Fengzhuang().findelement().send_keys('000111')
        # Fengzhuang().findelement().click()
        #
        # return Shouye()
        self.url("https://tea.codejiang.com/login")
        self.find(By.CSS_SELECTOR,'.el-form>div:nth-child(1) input').send_keys("guohongxia")
        self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(2) input').send_keys("000111")
        self.find(By.XPATH, '//*[@id="app"]/section/div/main/div/form/div[3]/div/div[1]').click()
        return Shouye(self.driver)





