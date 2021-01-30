from appium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': 'vivo_Y66i_A',
            'automationName': 'UiAutomator2',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'noReset':True,
            'chromedriverExecutable':'E:\迅雷下载\chromedriver',
            'dontStopAppOnReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown(self):
        pass

    def test_learn(self):
        print(self.driver.contexts)
        self.driver.find_element(By.ID,'com.tencent.mm:id/giv').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/div[2]').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[4]/div/div/ul/li[2]').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[5]/div[2]/div/div[1]').click()

