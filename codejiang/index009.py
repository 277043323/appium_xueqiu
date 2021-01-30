from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from codejiang.Menu_notic import GongGao
from codejiang.basepage import Base


class Shouye(Base):
    def shouye(self):
        sleep(6)
        self.find(By.XPATH,'//*[@class="container-top-control"]').click()
        # js = "document.querySelector('.menu-span').style.display='block'"
        js ="document.querySelector('.menu-span>li:nth-child(6) li').style.display='block'"
        self.js(js)
        self.find(By.XPATH,'//*[@class="menu-span"]/li[6]/div').click()
        sleep(5)
        self.find(By.XPATH,'//*[@class ="menu-span"]/li[6]//li[1]').click()
        return GongGao(self.driver)
