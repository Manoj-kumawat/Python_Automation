'''
Created on 24-Jul-2018

@author: admin
'''

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as cl
import logging
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumDriver():
    log = cl.CustomeLogger(logging.DEBUG)
    
    def __init__(self, driver):
        self.driver = driver
        
    def screenShot(self, resultMessage):
        fileName = resultMessage+"."+str(round(time.time()*1000))+".png"
        BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DESTINATION_DIRECTORY = os.path.join(BASEDIR,"screenshot")
        DESTINATION_FILENAME = os.path.join(DESTINATION_DIRECTORY,fileName)
        try:
            if not os.path.exists(DESTINATION_DIRECTORY):
                os.mkdir(DESTINATION_DIRECTORY)
            self.driver.save_screenshot(DESTINATION_FILENAME)
            self.log.info("Screenshot save to directory "+DESTINATION_FILENAME)
            
        except:
            self.log.error("###Exception Occured")
            print_stack()
        
    
    def getPageTitle(self):
        return self.driver.title
    
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == 'partialLink':
            return By.PARTIAL_LINK_TEXT
    
    def getElement(self, locator, locatorType="id" ):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element
    
    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element_list = None
        try:
            byType = self.getByType(locatorType)
            element_list = self.driver.find_elements(byType, locator)
            self.log("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
            
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element_list
    
    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
    
    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:# This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
    
    def getText(self, locator="", locatorType="id", element=None, info=""):
        elementText = None
        try:
            if locator:# This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            elementText = element.text
            self.log.debug("After finding element, size is: " + str(len(elementText)))
            if len(elementText) == 0:
                elementText = self.driver.get_attribute("innerText")
            if len(elementText) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + elementText + "'")
                elementText = elementText.strip()
        
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            elementText = None
        return elementText
    
    def selectElement(self, value, locator="", locatorType="", selectBy="text", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            select = Select(element)
            if selectBy == "index":
                select.select_by_index(value)
            elif selectBy == "value":
                select.select_by_value(value)
            else:
                select.select_by_visible_text(value)
            self.log.debug("Select the value "+value+" from dropDown on element with locator: " + locator + " locatorType: " + locatorType)
            return True
        except:
            self.log.error("Select the value "+value+" from dropDown on element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
            return False
        
    def switchToDefaultContent(self):
        self.driver.switch_to_default_content()
        self.log.debug("Switched to default content")
        
    def switchToFrame(self, locator=""):
        try:
            self.driver.switch_to_frame(locator)
            self.log.debug("Switched to frame with locator "+locator)
        except:
            self.log.error("Failed to switch frame with locator "+locator)
            print_stack()
            
    def isElementPresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False
        
    def isElementDisplayed(self, locator="", locatorType="", element=None):
        
        isDisplayed = False
        try:
            if locator:# This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType) 
            return isDisplayed   
        except:
            print("Element not found")
            return False

            
    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
            
    def webScroll(self, direction="up"):
        if direction.lower() == "up":
            #Scroll up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")
        
        self.log.info("Element appeared on the web page")
    
    def webScroll_JavaScript_Executor(self, locator="", locatorType="", element = None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.log.info("Element appeared on web page with locator "+locator)
        except:
            self.log.error("Failed to webpage scroll with locator "+locator)
            print_stack()
    
    def moveToElementAndClick(self, locator="", locatorType="", element = None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            action = ActionChains(self.driver)
            action.move_to_element(element).click(element).perform()
            self.log.info("Click on element with locator "+locator+" locator type "+locatorType)
        except:
            self.log.error("Can not Click on element with locator "+locator+" locator type "+locatorType)
            print_stack()
            
     
    
    