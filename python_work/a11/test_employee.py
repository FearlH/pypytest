import unittest
from employee import Employee as Em
class test_employee_functon(unittest.TestCase):
    def setUp(self):
        self.test_employee=Em("aaa","bbb",30000)
    def test_give_raise(self):
        print(f"1 {self.test_employee.salary}")
        self.test_employee.give_raise(10000)
        print(f"2 {self.test_employee.salary}")
        self.assertEqual(self.test_employee.salary,40000)
        print(f"3 {self.test_employee.salary}")
    def test_give_default_raise(self):
        print(f"4 {self.test_employee.salary}")
        self.test_employee.give_raise()
        print(f"5 {self.test_employee.salary}")
        self.assertEqual(self.test_employee.salary,35000)
        print(f"6 {self.test_employee.salary}")
if __name__=="__main__":
    unittest.main()