def encrypt_vigenere(plaintext, keyword):
    ciphertext = ''
    for index, ch in enumerate(plaintext):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= ch <= 'z' else ord('A')
            code = ord(ch) + shift
            if 'a' <= ch <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= ch <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            chiphertext += ch
    return ciphertext

p1=input("Enter you word: ")
k1=input("Enter you keyword: ")
print("Result:", encrypt_vigenere(p1,k1))