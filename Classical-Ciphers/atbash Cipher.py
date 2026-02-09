def atbash_cipher(text):
    encrypted = []
    for c in text:
        if c.isalpha():
            if c.islower():
                encrypted.append(chr(ord('z') - (ord(c) - ord('a'))))
            else:
                encrypted.append(chr(ord('Z') - (ord(c) - ord('A'))))
        else:
            encrypted.append(c)
    return ''.join(encrypted)

if __name__ == "__main__":
    print("atbash cipher in python")
    text = input("Enter the string to be encrypted:\n")
    print("Encrypted string:", atbash_cipher(text))