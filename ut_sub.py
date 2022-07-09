import unittest

def subtract(input_1, input_2):
    return (input_1 - input_2)

class SumTest(unittest.TestCase):

    def test_func2(self):
        # Arrange- create variable
        input_1 = 10
        input_2 = 20
        expected_output = 30
        # Act - call the function
        result = subtract(input_1, input_2)
        # result = input_1 - input_2
        print("Result:",result)
        # Assert- assert Result  
        self.assertNotEqual(result, expected_output, msg="result and expected output are NOT same")

if __name__ == '__main__':
    unittest.main()