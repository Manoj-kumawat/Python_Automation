import traceback
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    
    log  = cl.CustomeLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
        #locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
        
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")
    
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)
        
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
    
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")
        
        
        
    def login(self, username="", password=""):
        try:
            self.clickLoginLink()
            self.enterEmail(username)
            self.enterPassword(password)
            self.clickLoginButton()
            #error = self.getElementText("div[class$='alert-danger']", locatorType="css")
            #print("Login Failed"+error)
        except Exception:
            traceback.print_exc()
    
    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']", 
                                       locatorType='xpath')
        return result
    
    def verifyLoginFailed(self):
        result = self.isElementPresent("div[class$='alert-danger']", 
                                       locatorType='css')
        return result        

    def verifyPageTitle(self):
        print("-----"+self.getPageTitle())
        if "Google" in self.getPageTitle():
            return True
        else:
            False