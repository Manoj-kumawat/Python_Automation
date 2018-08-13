
#from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):
    
    log  = cl.CustomeLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
        #locators
    _home_img = "//span[contains(text(),'Kode It')]/following-sibling::img"
    _my_courses = "//a[contains(text(),'My Courses')]"
    _all_courses = "//a[contains(text(),'All Courses')]"
    _practice = "//a[contains(text(),'Practice')]"
    _user_icon = "//img[contains(@src,'avatar')]"
        
    def navigateToHome(self):
        self.moveToElementAndClick(locator=self._home_img, locatorType="xpath")
        
    def navigateToMyCourses(self):
        self.moveToElementAndClick(locator=self._my_courses, locatorType="xpath")
    
    def navigateToAllCourses(self):
        self.moveToElementAndClick(locator=self._all_courses, locatorType="xpath")
    
    def navigateToPractice(self):
        self.moveToElementAndClick(locator=self._practice, locatorType="xpath")        
    
    def navigateToUserSettings(self):
        self.elementClick(locator=self._user_icon, locatorType="xpath")
    
