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
            code = ord(symbol) + 3
            if code > ord('Z') and code < ord('a') or code > ord('z'):
                code -= 26
            letter = chr(code)
            cipherText += letter
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
            if code < ord('a') and code > ord('Z') or code < ord('A'):
                code += 26
            letter = chr(code)
            plaintext += letter
        else:
            plaintext += symbol
    return plaintext
