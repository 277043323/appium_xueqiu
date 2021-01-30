import yaml
from selenium.webdriver.common.by import By

from codejiang.basepage import Base

class Fengzhuang(Base):

    def findelement(self):

        self.base().find_element(By.XPATH,
                                 '//*[@id="app"]/section/div/main/div/form/div[1]/div/div[1]/input')
        self.base().find_element(By.XPATH,'//*[@id="app"]/section/div/main/div/form/div[2]/div/div[1]/input')
        self.base().find_element(By.XPATH, '//*[@id="app"]/section/div/main/div/form/div[3]/div/div[1]')




    def get_url(self,url):
        self.base().get(url)







