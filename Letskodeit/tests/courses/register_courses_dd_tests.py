'''
Created on 09-Aug-2018

@author: admin
'''
import unittest
from pages.courses.register_courses_page import RegisterCoursesPage
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def objectSetUp(self,oneTimeSetUp):
        if self.driver is None:
            assert False
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
    
    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234567891237896", "0123", "198", "Algeria", "122001"))
    @unpack
    def test_enrollForCourse(self, courseName, cc_num, cc_exp, cc_cvv, country, postal_code):
        self.rcp.selectCategoryAndAuthor("All", "All")
        self.rcp.enterCourseName(courseName)
        self.rcp.clickOnCourseName(courseName)
        self.rcp.enrollCourse(cc_num=cc_num, cc_exp=cc_exp, cc_cvv=cc_cvv, country=country, postal=postal_code)
        self.ts.markFinal("enrollForCourse", "Pass", "Successfully enrolled for course")
        
        
