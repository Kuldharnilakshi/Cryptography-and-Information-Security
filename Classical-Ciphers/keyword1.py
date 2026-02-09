
def generate_cipher_alphabet(keyword):
    keyword = keyword.lower()
    result = ""
    for char in keyword:
        if char not in result and char.isalpha():
            result += char
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in result:
            result += char
    return result

def encrypt(text, keyword):
    cipher_alphabet = generate_cipher_alphabet(keyword)
    result = ""
    for char in text:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            new_char = cipher_alphabet[index]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def decrypt(cipher_text, keyword):
    cipher_alphabet = generate_cipher_alphabet(keyword)
    result = ""
    for char in cipher_text:
        if char.isalpha():
            index = cipher_alphabet.find(char.lower())
            new_char = chr(index + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

# --- Main Program ---
print("Keyword Cipher in Python")
choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

text = input("Enter the text: ")
keyword = input("Enter the keyword: ")

if choice == 'e':
    encrypted = encrypt(text, keyword)
    print("Encrypted Text:", encrypted)
elif choice == 'd':
    decrypted = decrypt(text, keyword)
    print("Decrypted Text:", decrypted)
else:
    print("Invalid choice! Enter 'e' for encrypt or 'd' for decrypt.")
