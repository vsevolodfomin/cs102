def encrypt_caesar(plaintext):
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


if __name__ == '__main__':
    p1 = input("Enter you encript word: ")
    print("Crypt:", encrypt_caesar(p1))
    k1 = input("Enter you crypt word: ")
    print(":", decrypt_caesar(k1))
