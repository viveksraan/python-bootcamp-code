''' 
This file is to use unittest packages's TestCase class to perform various types of tests on your python. But remember two things

1- you don't have to instantiate TestCap class manually as Here, you are instantiating the TestCap class (test1 = TestCap()) manually.
That’s not needed — the unittest framework automatically creates test instances and runs all methods that start with test_.
So manually creating test1 does nothing useful, and can even cause confusion.

2-  If you are the "python -m unittest test_cap.py" then it's fine other wise if you want to use "python test_cap.py" command use it in cmd not in vs code integrated terminal or else change settings for running the code in VS code.  
'''

import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        '''
        This method tests that cap_text function in cap.py is converting the letters for all one word texts to required format only which is first letter of the word capital. Now if there would be any issue in that function the TestCap class which is built upon builtin unittest.TestCase class will inform us
        '''
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_word(self):
        '''
        This method tests that cap_text function in cap.py is converting the letters of all multi word texts to required format only which is first letter of the opening word in the string capital rest of the words all letters small. Now if there would be any issue in that function the TestCap class which is built upon builtin unittest.TestCase class will inform us. For example currently the test_cap function is using capitalize method which capitalizes first letter of the first word in the string capital but what we want is first letter of every word in the string capital so TestCap.test_multiple_word will inform us about this issue. We can switch to title method which will then capitalize first letter of every word and our bug would be resolved
        '''
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()