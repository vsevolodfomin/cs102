def encrypt_vigenere(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        if 65 <= plaintext_int[i] <= 90:
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        elif 97 <= plaintext_int[i] <= 122:
            # 12 - change between alphabets 
            value = (plaintext_int[i] + key_as_int[i % key_length] - 12) % 26
            ciphertext += chr(value + 97)
        else:
            ciphertext += chr(plaintext_int[i])
    return ciphertext


def decrypt_vigenere(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        if 65 <= ciphertext_int[i] <= 90:
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        elif 97 <= ciphertext_int[i] <= 122:
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 97)
        else:
            plaintext += chr(ciphertext_int[i])
    return plaintext


p1 = input("Enter you word: ")
k1 = input("Enter you keyword: ")
n1 = encrypt_vigenere(p1, k1)
print("Result encript:", n1)
print("Result decripr", decrypt_vigenere(n1, k1))