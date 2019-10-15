import unittest
import vigener



class vigenereCipherTest(unittest.TestCase):

    def test_encrypt_empty_string(self):
        self.assertEqual(vigener.encrypt_vigenere("",""), "")

    def test_encrypt_uppercase(self):
        self.assertEqual(vigener.encrypt_vigenere("PYTHON","A"), "PYTHON")

    def test_encrypt_lowercase(self):
        self.assertEqual(vigener.encrypt_vigenere("python","a"), "python")

    def test_encrypt_uppercase_Long_key(self):
        self.assertEqual(vigener.encrypt_vigenere("VSEVOLOD","ZAQ"), "USUUOBND")

    def test_encrypt_uppercase_lowercase_and_digits_Long_key(self):
        self.assertEqual(vigener.encrypt_vigenere("Python3.6","zAq"), "Usjgid3.6")

    def test_decrypt_empty_string(self):
        self.assertEqual(vigener.decrypt_vigenere("",""), "")

    def test_decrypt_uppercase(self):
        self.assertEqual(vigener.decrypt_vigenere("PYTHON","A"), "PYTHON")

    def test_decrypt_lowercase(self):
        self.assertEqual(vigener.decrypt_vigenere("python","a"), "python")

    def test_decrypt_uppercase_and_Long_key(self):
        self.assertEqual(vigener.decrypt_vigenere("USUUOBND","ZAQ"), "VSEVOLOD")

    def test_decrypt_uppercase_lowercase_and_digits_Long_key(self):
        self.assertEqual(vigener.decrypt_vigenere("Usjgid3.6","zAq"), "Python3.6")
