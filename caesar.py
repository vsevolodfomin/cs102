def encrypt_caesar(plaintext):
    cipherText = ""
    for symbol in plaintext:
        if symbol.isalpha():
            cod = ord(symbol) + 3
            if cod > ord('z'):
                cod -= 26
            Letter = chr(cod)
            cipherText += Letter
    return cipherText
    
def decrypt_caesar(ciphertext):
    plaintext = ""
    for symbol in ciphertext:
        if symbol.isalpha():
            cod = ord(symbol) - 3
            if cod > ord('z'):
                cod +=26
            Letter = chr(cod)
            plaintext += Letter

    return plaintext


p1=input("Enter you encript word: ")
print("Crypt:", encrypt_caesar(p1))
k1=input("Enter you crypt word: ")
print(":", decrypt_caesar(k1))
