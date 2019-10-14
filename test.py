plaintext = "abc" 
key = "def"
key_length = len(key)
key_as_int = [ord(i) for i in key]
plaintext_int = [ord(i) for i in plaintext]
ciphertext = ''

for i in range(len(plaintext_int)):
    if 65 <= plaintext_int[i] <= 90:
        print(i)
        print( key_as_int[i])
        print( key_as_int[i % key_length])
        print(plaintext_int[i])
        print(plaintext_int[i] + key_as_int[i % key_length])
        print((plaintext_int[i] + key_as_int[i % key_length]) % 26)
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        print(value)
        ciphertext += chr(value + 65)
        print(ciphertext)
    elif 97 <= plaintext_int[i] <= 122:
        print(i)
        print( key_as_int[i])
        print( key_as_int[i % key_length])
        print(plaintext_int[i])
        print(plaintext_int[i] + key_as_int[i % key_length])
        print((plaintext_int[i] + key_as_int[i % key_length] - 12) % 26)
        
        value = (plaintext_int[i] + key_as_int[i % key_length] - 12) % 26
        print(value)
        
        
        ciphertext += chr(value + 97)
        print(ciphertext)
    else:
        ciphertext += chr(ciphertext_int[i])#***

print("Decrypt", ciphertext)

ciphertext_int = [ord(i) for i in ciphertext]
plaintext = ''
for i in range(len(ciphertext_int)):
    #if 65 < ciphertext_int[i] < 97:
    if 65 <= ciphertext_int[i] <= 90:
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        print(value)
        plaintext += chr(value + 65)
        print(plaintext)
    elif 97 <= ciphertext_int[i] <= 122:
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        print(value)
        plaintext += chr(value + 97)
        print(plaintext)
    else:
        plaintext += chr(ciphertext_int[i]) #***

print("Encrypt", plaintext)
