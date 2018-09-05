'''
Created on 09-Aug-2018

@author: admin
'''
import unittest
from pages.courses.register_courses_page import RegisterCoursesPage
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
import os
from utilities.read_data import getExcelData
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):
    
    BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    TESTDATA_FILE_PATH = os.path.join(BASEDIR,'test_data_sheet.xlsx')
    
    @pytest.fixture(autouse=True)
    def objectSetUp(self,oneTimeSetUp):
        if self.driver is None:
            assert False
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.np = NavigationPage(self.driver)
        
    def setUp(self):
        self.rcp.webScroll("up")
        self.np.navigateToHome()
    
    @pytest.mark.run(order=1)
    @data(*getExcelData(TESTDATA_FILE_PATH,'TestData'))
    @unpack
    def test_enrollForCourse(self, courseName, cc_num, cc_exp, cc_cvv, country, postal_code):
        self.rcp.selectCategoryAndAuthor("All", "All")
        self.rcp.enterCourseName(courseName)
        self.rcp.clickOnCourseName(courseName)
        self.rcp.enrollCourse(cc_num=cc_num, cc_exp=cc_exp, cc_cvv=cc_cvv, country=country, postal=postal_code)
        self.ts.markFinal("enrollForCourse", "Pass", "Successfully enrolled for course")
        
