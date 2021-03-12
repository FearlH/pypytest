import unittest
from city_function import city_name as cn
class TestCities(unittest.TestCase):
    def test_city_function_city_name(self):
        self.assertEqual(cn("aaa","bbb",1000),"Aaa,Bbb - population 1000")
    def test_city_name_population(self):
        self.assertEqual(cn("aaa","bbb"),"Aaa,Bbb")
if __name__=="__main__":
    unittest.main()