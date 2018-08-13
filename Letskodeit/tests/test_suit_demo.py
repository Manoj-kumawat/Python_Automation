'''
Created on 12-Aug-2018

@author: admin
'''

import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_CSV_data_tests import RegisterCoursesTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTests)

smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)