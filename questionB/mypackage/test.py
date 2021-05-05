from versionFunction import versionChecker
import unittest

class TestVersionChecker(unittest.TestCase):
    
    #equal test
    def test_1_equal(self):

        result =versionChecker(2,2) 
        temp = "2 version is equal to version 2"
        self.assertEqual(result, temp)
    
    def test_2_equal(self):

        result =versionChecker(1,2) 
        temp = "1 version is equal to version 2"
        self.assertNotEqual(result, temp)

    #smaller test
    def test_3_smaller(self):

        result =versionChecker(2.1,2.2) 
        temp = "2.1 version is smaller than version 2.2"
        self.assertEqual(result, temp)
    
    def test_4_smaller(self):

        result =versionChecker(2.4,2.2) 
        temp = "2.4 version is smaller than version 2.2"
        self.assertNotEqual(result, temp)
    
    #larger test
    def test_5_larger(self):

        result =versionChecker(2.7,2.3) 
        temp = "2.7 version is larger than version 2.3"
        self.assertEqual(result, temp)
    
    def test_6_larger(self):

        result =versionChecker(1.7,2.3) 
        temp = "1.7 version is larger than version 2.3"
        self.assertNotEqual(result, temp)




if __name__ == '__main__':
    unittest.main()