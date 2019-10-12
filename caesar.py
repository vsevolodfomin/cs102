def encrypt_caesar(plaintext):
    ciphertext = ''
    for ch in plaintext:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            code = ord(ch) + 3
            if code > ord('Z') and code < ord('a') or code > ord('z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext):
    plaintext = ''
    for ch in ciphertext:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            code = ord(ch) - 3
        if code < ord('a') and code > ord('Z') or code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += ch
    return plaintext


p1=input("Enter you encript word: ")
print("Crypt:", encrypt_caesar(p1))
k1=input("Enter you crypt word: ")
print(":", decrypt_caesar(k1))