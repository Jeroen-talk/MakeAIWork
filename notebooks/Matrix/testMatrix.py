#!/usr/bin/env python

import unittest
from class Matrix import class_Matrix

'''
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    employee1 = Employee(firstName="Marc", lastName="Rotsaert", pay=6000, bonus=500)
    employee2 = Employee(firstName="Anton", lastName="Diepenhorst", pay=4500, bonus=1000)

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.employee1.fullname, 'Marc Rotsaert')
        self.assertEqual(self.employee2.fullname, 'Anton Diepenhorst')

    def test_annualSalary(self):
        print('test_apply_raise')
        self.employee1.annualSalary
        self.employee2.annualSalary

if __name__ == '__main__':
    unittest.main()
'''


class TestMatrix(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(setUpClass)

    vectorTestList1 = vectorList1([1, 2, 3], [4, 5, 6])
    vectorTestList2 = vectorList2([1, 1, 1], [1, 1, 1])

    def testVectorList(self):
        print('testVectorList')
        self.assertEqual(self.vectorTestList1.matrix1, [1, 2, 3], [4, 5, 6])


if __name__ == '__main__':
    unittest.main()
