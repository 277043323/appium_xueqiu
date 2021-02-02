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
        # self.url("https://tea.codejiang.com/login")
        #yaml文件管理数据
        # url = (yaml.safe_load(open("E:\\Ghx_Work_Project\\appium_xueqiu\\codejiang\\common\\data.yaml")))["url"]
        url = (yaml.safe_load(open("common/data.yaml")))["url"]
        self.url(url)
        key01 = (yaml.safe_load(open("common\\data.yaml")))["username"]
        key02 =(yaml.safe_load(open("common\\data.yaml")))["passwd"]
        path01 = (yaml.safe_load(open("common\\data.yaml")))["CSS_SELECTOR"][0]
        path02 = (yaml.safe_load(open("common\\data.yaml")))["CSS_SELECTOR"][1]
        # self.find(By.CSS_SELECTOR,'.el-form>div:nth-child(1) input').send_keys("guohongxia")
        # self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(1) input').send_keys(key01)
        self.find(By.CSS_SELECTOR, path01).send_keys(key01)
        self.find(By.CSS_SELECTOR, path02).send_keys(key02)
        # self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(1) input').send_keys(key01)
        # self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(2) input').send_keys(key02)
        # self.find(By.CSS_SELECTOR, '.el-form>div:nth-child(2) input').send_keys("000111")

        self.find(By.XPATH, '//*[@id="app"]/section/div/main/div/form/div[3]/div/div[1]').click()
        return Shouye(self.driver)





