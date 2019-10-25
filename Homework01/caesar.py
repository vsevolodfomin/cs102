def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    
    cipherText = ""
    for symbol in plaintext:
        if symbol.isalpha():
            cod = ord(symbol) + 3
            if cod > ord('Z') and cod < ord('a') or cod > ord('z'):
                cod -= 26
            Letter = chr(cod)
            cipherText += Letter
        else:
            cipherText += symbol
    return cipherText
    

def decrypt_caesar(cipherText):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for symbol in cipherText:
        if symbol.isalpha():
            cod = ord(symbol) - 3
            if cod < ord('a') and cod > ord('Z') or cod < ord('A'):
                cod += 26
            Letter = chr(cod)
            plaintext += Letter
        else:
            plaintext += symbol
    return plaintext


if __name__ == "__main__":
    import doctest
    doctest.testmod()
