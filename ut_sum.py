import unittest

class SumTest(unittest.TestCase):
    
    def test_func1(self):
        # Arrange- create variable
        input1 = 10
        input2 = 20
        expected_output = 40
        # Act - call the function
        # result = sum(input1, input2)
        result = input1 + input2
        print("Result:",result)
        # Assert- assert Result  
        self.assertEqual(result, expected_output, msg="result and expected output are NOT same")

if __name__ == '__main__':
    unittest.main()