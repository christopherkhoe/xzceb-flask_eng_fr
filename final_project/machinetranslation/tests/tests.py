import unittest
from translator import en_to_fr, fr_to_en

class TestEnglishToFrench(unittest.TestCase):
    def test_1(self):
        """Test assertEqual"""
        self.assertEqual(en_to_fr('Hello'), 'Bonjour')
    def test_2(self):
        """Test assertNotEqual"""
        self.assertNotEqual(en_to_fr('Hello'), None)
    def test_3(self):
        """Test assertEqual"""
        self.assertEqual(en_to_fr("Good night"), "Bonne nuit")

class TestFrenchToEnglish(unittest.TestCase):
    def test_1(self):
        """Test assertEqual"""
        self.assertEqual(fr_to_en('Bonjour'), 'Hello')
    def test_2(self):
        """Test assertNotEqual"""
        self.assertNotEqual(fr_to_en('Bonjour'), None)
    def test_3(self):
        """Test assertEqual"""
        self.assertEqual(fr_to_en('Bonne nuit'), 'Good night')

unittest.main()