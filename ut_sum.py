import unittest
    
class SumTest(unittest.TestCase):
    
    def sum(input1, input2):
        return input1 + input2
        
    def sum_testfunc_1(self):
        # Arrange- create variable
        input1 = 10
        input2 = 20
        expected_output = 30
        # Act - call the function
        result = sum(input1, input2)
        print("Result:",result)
        # Assert- assert Result  
        self.assertEqual(result, expected_output, msg="result and expected output are same")
    
if __name__ == '__main__':
    unittest.main()