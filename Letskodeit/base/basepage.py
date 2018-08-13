
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
from lib2to3.tests.support import driver

class BasePage(SeleniumDriver):
    
    def __init__(self, driver):    
        """
            Inits BasePage class
    
            Returns:
                None
        """
        super().__init__(driver)
        self.driver = driver 
        self.util = Util()
        
    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualPageTitle = self.getPageTitle()
            return self.util.verifyTextContains(actualPageTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

        