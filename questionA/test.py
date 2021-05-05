from overlapFunction import checkOverLapse
import unittest

class TestcheckOverLapse(unittest.TestCase):
    
    #equal test
    def test_1_overlap(self):

        result =checkOverLapse(-10,90,1,6)
        temp = "2 lines overlap"
        self.assertEqual(result, temp)

    def test_2_overlap(self):

        result =checkOverLapse(1,5,2,6)
        temp = "2 lines overlap"
        self.assertEqual(result, temp)

    def test_3_overlap(self):

        result =checkOverLapse(1,5,6,8)
        temp = "2 lines overlap"
        self.assertNotEqual(result, temp)

    def test_4_doesNotOverlap(self):

        result =checkOverLapse(-10,0,2,6)
        temp = "2 lines does not overlap"
        self.assertEqual(result, temp)
    
    def test_5_doesNotOverlap(self):

        result =checkOverLapse(-10,-5,-2,1)
        temp = "2 lines does not overlap"
        self.assertEqual(result, temp)
    
    def test_6_doesNotOverlap(self):

        result =checkOverLapse(-10,-5,-6,1)
        temp = "2 lines does not overlap"
        self.assertNotEqual(result, temp)
    

if __name__ == '__main__':
    unittest.main()