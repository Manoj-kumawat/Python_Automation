import os


from selenium import webdriver
from traceback import print_stack
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WebDriverFactory():
    
    BASE_URL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    def __init__(self, browser):
        
        self.browser = browser

    def getWebdriverInstance(self,baseurl):
        driver = None
        try:
            if self.browser == "iexplorer":
                #set ie driver
                driver = webdriver.Ie()
            
            elif self.browser == "firefox":
                GECKO_DRIVER_PATH = os.path.join(os.path.join(self.BASE_URL,'driver'), 'geckodriver.exe')
                #os.environ["webdriver.chrome.driver"] = CHROME_DRIVER_PATH
                driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
            
            elif self.browser == "chrome":
                CHROME_DRIVER_PATH = os.path.join(os.path.join(self.BASE_URL,'driver'), 'chromedriver.exe')
                os.environ["webdriver.chrome.driver"] = CHROME_DRIVER_PATH
                options = webdriver.ChromeOptions()
                options.add_argument('--ignore-certificate-errors')
                options.add_argument("--test-type")
                #options.binary_location = "/usr/bin/chromium"
                driver = webdriver.Remote(command_executor="http://192.168.31.36:5566/wd/hub", desired_capabilities=DesiredCapabilities.CHROME )
                #driver = webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER_PATH)
            
            else:
                driver = webdriver.Firefox()
            
            driver.set_page_load_timeout(60)
            driver.implicitly_wait(15)
            driver.maximize_window()
            driver.get(baseurl)
            return driver
        
        except :
            print("Driver initialization failed")
            print_stack()
            #traceback.print_stack()
            return driver