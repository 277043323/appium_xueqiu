from time import sleep

from selenium.webdriver.common.by import By

from codejiang.Menu_notic import GongGao
from codejiang.basepage import Base


class Shouye(Base):
    def shouye(self):
        self.find(By.XPATH,'//*[@class="container-top-control').click()
        sleep(5)
        self.find(By.XPATH,'//*[@class ="menu-span"]/li[6]').click()
        sleep(5)
        self.find(By.XPATH,'//*[@class ="menu-span"]/li[6]//li[1]').click()
        sleep(5)
        return GongGao()
