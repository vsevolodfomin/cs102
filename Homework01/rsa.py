import random
import sys


def is_prime(n):
    """
    Check for a simple number.
    >>> is_prime(17)
    True
    >>> is_prime(20)
    False
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """
    Function to find the largest common divisor.
    >>> gcd(17,23)
    1
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    # PUT YOUR CODE HERE
    div1 = float()
    d = 0 
    div1 = ((d * e) - 1) / phi
    for d in range (sys.maxsize) :
        div1 = ((d * e) - 1) / phi
        if (div1).is_integer()==True:
            break
        else:
            d += 1
    return d


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    # PUT YOUR CODE HERE

    phi = (p-1) * (q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    """
    Encrypts RSA.
    >>> encrypt((13, 221),"Hello")
    [72, 101, 95, 95, 59]
    
    """
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    """
    Decrypts RSA.
    >>> decrypt((133, 221),[72, 101, 95, 95, 59])
    'Hello'
    """
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)
