'''
Created on 09-Aug-2018

@author: admin
'''

from base.basepage import BasePage
import logging
import utilities.custom_logger as cl

class RegisterCoursesPage(BasePage):
    log = cl.CustomeLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver
    
    _all_courses = "//a[contains(text(),'All Courses')]" #all courses link
    _category_button = "//div[contains(text(), 'Category')]/..//following-sibling::button"
    _category_type = "//div[contains(text(), 'Category')]/..//following-sibling::li/a[text()='{0}']"
    _author_button = "//div[contains(text(), 'Author')]/..//following-sibling::button"
    _author_type = "//div[contains(text(), 'Author')]/..//following-sibling::li/a[text()='{0}']"
    _search_box = "query" #input search for course locator tpe name
    _course= "//div[@class='course-listing-title' and contains(text(),'{0}')]" #course 
    _enroll_button = "enroll-button-top" #Enroll button id
    _payment_information = "//h1[text()='Payment Information']" #Payment Information for scrolling page locator type text
    _cc_num = "//*[@aria-label='Credit or debit card number']" # name of the field
    _cc_exp = "exp-date" #name of the field
    _cc_cvv = "cvc" #name of he field
    _country = "country_code" #name of the field
    _postal_code = "postal" #locator Type name
    _agree_to_terms = "agreed_to_terms_checkbox" #locator type name
    
    _card_num_frame = "__privateStripeFrame4" #locator type Name
    _exp_date_frame = "__privateStripeFrame5" #locator type Name
    _cvv_frame = "__privateStripeFrame6" # Locator type Name
    _postal_code_frame = "__privateStripeFrame7" #locator type name
    
    def selectCategoryAndAuthor(self, categoryType, authorType):
        self.waitForElement(locator=self._all_courses, locatorType="xpath", timeout=30)
        self.elementClick(locator=self._all_courses, locatorType="xpath")
        self.waitForElement(locator = self._category_button, locatorType="xpath", timeout=30)
        self.elementClick(locator = self._category_button, locatorType="xpath")
        self.elementClick(locator = self._category_type.format(categoryType), locatorType="xpath")
        self.elementClick(locator = self._author_button, locatorType="xpath")
        self.elementClick(locator = self._author_type.format(authorType), locatorType="xpath")
        
    
    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="name")
    
    def clickOnCourseName(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")
    
    def clickToEnrollInCourse(self):
        self.elementClick(locator=self._enroll_button, locatorType="id")
    
    def scrollIntoViewPayemtInformation(self):
        self.webScroll_JavaScript_Executor(locator=self._payment_information, locatorType="xpath")
        
    
    def enterCardNum(self, cc_Num):
        self.switchToDefaultContent()
        self.switchToFrame(locator=self._card_num_frame)
        self.sendKeys(cc_Num, locator=self._cc_num, locatorType="xpath")
    
    def enterExpDate(self, expDate):
        self.switchToDefaultContent()
        self.switchToFrame(locator=self._exp_date_frame)
        self.sendKeys(expDate,locator=self._cc_exp, locatorType="name" )
        
    
    def enterCvv(self, cvv):
        self.switchToDefaultContent()
        self.switchToFrame(locator=self._cvv_frame)
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
    
    def selectCountry(self, country):
        self.switchToDefaultContent()
        self.selectElement(country, locator=self._country, locatorType="name", selectBy="text")
    
    def enterPostalCode(self, postalCode):
        self.switchToDefaultContent()
        self.switchToFrame(locator=self._postal_code_frame)
        element = self.getElement(locator=self._postal_code, locatorType="name")
        self.elementClick(element=element)
        self.sendKeys(postalCode, element= element)
        self.switchToDefaultContent()
    
    def clickOnAgreeTerms(self):
        self.elementClick(locator=self._agree_to_terms, locatorType="id")
        
    def enterCreditCardInFormation(self, num, exp, cvv, country, postal):
        self.scrollIntoViewPayemtInformation()
        self.enterCardNum(num)
        self.enterExpDate(exp)
        self.enterCvv(cvv)
        self.selectCountry(country)
        self.enterPostalCode(postal)
        self.clickOnAgreeTerms()
        
    def enrollCourse(self, cc_num="", cc_exp="", cc_cvv="", country="", postal="" ):

        self.clickToEnrollInCourse()
        self.enterCreditCardInFormation(cc_num, cc_exp, cc_cvv, country, postal)
        
    
    
