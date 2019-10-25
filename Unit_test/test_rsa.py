import unittest
import rsa


class rsaCipherTest(unittest.TestCase):

    def test_is_prime_true(self):
        self.assertEqual(rsa.is_prime(17), True)


    def test_is_prime_false(self):
        self.assertEqual(rsa.is_prime(20), False)


    def test_multiplicative_inverse(self):
        self.assertEqual(rsa.multiplicative_inverse(7,40), 23)


    def test_generate_keypair(self):
        public, private = rsa.generate_keypair(17,23)
        self.assertEqual(private[1], 391)
        self.assertEqual(public[1], 391)


    def test_gsd(self):
        self.assertEqual(rsa.gcd(17, 23), 1)


    def test_encrypt(self):
        self.assertEqual(rsa.encrypt((13, 221),"Hello"), [72, 101, 95, 95, 59])


    def test_decrypt(self):
        self.assertEqual(rsa.decrypt((133, 221),[72, 101, 95, 95, 59]),"Hello")

