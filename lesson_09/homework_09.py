import unittest
from homeworks import average, list_of_numbers

class TestEvarageFunction(unittest.TestCase):
    def test_evarage(self):
        result = average(list_of_numbers)
        expected = sum(list_of_numbers)/len(list_of_numbers)
        self.assertEqual(result, expected)

    def test_evarage_not_0(self):
        result = average(list_of_numbers)
        self.assertGreater(result, 0)

if __name__ == '__main__':
   unittest.main()

import unittest
from homeworks import longest_word, check_single_occurence, words

class TestLongestFunction(unittest.TestCase):
    def test_longest(self):
        result = longest_word(words)
        expected = "friend"
        self.assertEqual(result, expected)

    def test_single_occurence(self):
        result = check_single_occurence(words, 'friend')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


import unittest
from homeworks import is_even, list_1

class TestIsEvenFunction(unittest.TestCase):
    def test_even_number(self):
        is_even_numbers = list(filter(is_even, list_1 ))
        result = sum(is_even_numbers)
        expected = 32
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


import unittest
from homeworks import has_letter_h, word, word_2

class TestHasLetterInFunction(unittest.TestCase):
    def test_contain(self):
        result = has_letter_h(word)
        self.assertTrue(result)

    def test_not_contain(self):
        result = has_letter_h(word_2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()



import unittest
from homeworks import item, lst1, lst2

class TestIsInstanceFunction(unittest.TestCase):
    def test_contain(self):
        lst2.extend(filter(item,lst1))
        result = lst2
        self.assertTrue(result)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()


import unittest
from homeworks import list_unique, uni_str, uni_str_1

class TestHasUniqueInFunction(unittest.TestCase):
    def test_contain_more_than_10_unique(self):
        result = list_unique(uni_str)
        self.assertTrue(result)

    def test_contain_less_than_10_unique(self):
        result = list_unique(uni_str_1)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()