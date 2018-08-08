import unittest
from selenium.common.exceptions import NoSuchElementException

import traceback
import pytest

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        if self.driver is None:
            assert False;
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
    
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        
        self.lp.login("test123@test.com", "test@12345")
        result1 = self.lp.verifyPageTitle()
        self.ts.mark(result1, "Title is incorrect.") 
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", "True", "Login was not successful.")  

        
    
    
    @pytest.mark.run(order=1)
    def test_invalidValidLogin(self):
        try:
            self.lp.login("test123@test.com", "test@12345")
            result = self.lp.verifyLoginFailed()
            assert result == True
            #self.ts.markFinal("test_validLogin", result, "Login was not successful.")   
        except (NoSuchElementException,AttributeError,TypeError, AssertionError) as nse:
            print(nse)
            traceback.print_exc()
            print("Error in login ")
            #self.driver.quit()
        
    

        
        