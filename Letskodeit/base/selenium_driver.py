'''
Created on 24-Jul-2018

@author: admin
'''

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as cl
import logging
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import os
import time

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
    
    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
    
    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
    
    def getElementText(self, locator, locatorType="id"):
        elementText = None
        try:
            element = self.getElement(locator, locatorType)
            elementText = element.text
            self.log.info("Got element text with locator: " + locator + " locatorType: " + locatorType)
            return elementText
        except:
            self.log.info("Can not Get element text with locator: " + locator + " locatorType: " + locatorType)
            print_stack()
        return elementText
        
        
    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
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
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            self.log.info_stack()
        return element
