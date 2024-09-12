import unittest
from stringProgram import charNumberCount, vowelNumberCount, digitNumberCount

class TestStringFunctions(unittest.TestCase):

    def test_charNumberCount(self):
        print("\nTesting the first function charNumberCount...")
        
        #Empty String Test
        self.assertEqual(charNumberCount(""), 0, "Failed on empty string")
        
        #Single Char Test
        self.assertEqual(charNumberCount("a"), 1, "Failed on single character")
        self.assertEqual(charNumberCount(" "), 0, "Failed on single space")
        
        #Multiple Char Test
        self.assertEqual(charNumberCount("barsa"), 5, "Failed on 'barsa' a string without empty spaces")
        self.assertEqual(charNumberCount("    "), 0, "Failed on multiple spaces")
        self.assertEqual(charNumberCount("Hello darkness my old friend"), 24, "Failed on 'Hello darkness my old friend' a string with multiple spaces and char")
        self.assertEqual(charNumberCount("test 123 !@#"), 10, "Failed on string with number, alphabet, special characters and space")

    def test_vowelNumberCount(self):
        print("\nTesting the second function vowelNumberCount...")
        
        #Empty String Test
        self.assertEqual(vowelNumberCount(""), 0, "Failed on empty string")
        
        #Single Char Test
        self.assertEqual(vowelNumberCount("a"), 1, "Failed on single lowercase vowel character")
        self.assertEqual(vowelNumberCount("A"), 1, "Failed on single lowercase vowel character")
        self.assertEqual(vowelNumberCount("b"), 0, "Failed on single non vowel character")
        self.assertEqual(vowelNumberCount(" "), 0, "Failed on single space")
        
        #Multiple Char Test
        self.assertEqual(vowelNumberCount("aeiuo"), 5, "Failed on all lower case vowel string")
        self.assertEqual(vowelNumberCount("AEIUO"), 5, "Failed on all upper case vowel string")
        self.assertEqual(vowelNumberCount("PCKL"), 0, "Failed on all non vowel string")
        self.assertEqual(vowelNumberCount("    "), 0, "Failed on multiple spaces")
        self.assertEqual(vowelNumberCount("Hello Darkness My Old Friend"), 7, "Failed on 'Hello darkness my old friend' a string with multiple spaces and char")
        self.assertEqual(vowelNumberCount("test 123 !@#"), 1, "Failed on string with number, alphabet, special characters and space")

    def test_digitNumberCount(self):
        print("\nTesting the third function digitNumberCount...")
        
        #Empty String Test
        self.assertEqual(digitNumberCount(""), 0, "Failed on empty string")
        
        #Single Char Test
        self.assertEqual(digitNumberCount("0"), 1, "Failed on single digit")
        self.assertEqual(digitNumberCount("a"), 0, "Failed on single non digit")
        self.assertEqual(digitNumberCount(" "), 0, "Failed on single space")
        
        #Multiple Char Test
        self.assertEqual(digitNumberCount("0123456789"), 10, "Failed on all digit string")
        self.assertEqual(digitNumberCount("I am not digit"), 0, "Failed on all non digit string")
        self.assertEqual(digitNumberCount("    "), 0, "Failed on multiple spaces")
        self.assertEqual(digitNumberCount("Hell0 D4rkness My 0ld Fr1end"), 4, "Failed on 'Hell0 D4rkness My 0ld Fr1end' a string with multiple spaces and char")
        self.assertEqual(digitNumberCount("test 123 !@#"), 3, "Failed on string with number, alphabet, special characters and space")
        
#verbosity is very cool
if __name__ == '__main__':
    unittest.main(verbosity=1)
