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
    def test_enrollForCourse(self):
        self.rcp.selectCategoryAndAuthor("All", "All")
        self.rcp.enterCourseName("JavaScript for beginners")
        self.rcp.clickOnCourseName("JavaScript for beginners")
        self.rcp.enrollCourse("1234567891237896", "0123", "198", "Algeria", "122001")
        self.ts.markFinal("enrollForCourse", "Pass", "Successfully enrolled for course")
        
        
