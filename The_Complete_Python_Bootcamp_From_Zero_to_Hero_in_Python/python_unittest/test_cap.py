"""
    Unittest script to test cap.py file
"""

import unittest
import cap

class TestCap(unittest.TestCase):
    """
    Test class that defines
    the method to be used on cap.py file
    """
    def test_one_word(self):
        """
        Testing only single word string
        """
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multi_words(self):
        """
        Testing only multi word string
        """
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == "__main__":
    unittest.main()
