import unittest
from name_function import get_formatted_name as gfn
class NameTest(unittest.TestCase):
    def test_name(self):
        formated_name=gfn("aaa","bbb","ccc")
        self.assertEqual(formated_name,"Aaa Ccc Bbb")
if __name__=="__main__":
    unittest.main()
