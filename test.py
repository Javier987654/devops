import unittest
from funcionSumar import sumar

class testSumar(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(sumar(1, 2), 3)
        self.assertEqual(sumar(5, 5), 10)
        
if __name__ == '__main__':
    unittest.main()
