def monoalphabetic_encrypt(plain_text):
    plain_text = plain_text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "qwertyuiopasdfghjklzxcvbnm"

    cipher_text = ""

    for char in plain_text:
        if char.isalpha():
            index = alphabet.index(char)
            cipher_char = key[index]
            cipher_text += cipher_char
        else:
            cipher_text += char  # Keep spaces and punctuation
    return cipher_text

# --- User Input and Encryption ---
print("Monoalphabetic Cipher")
plain_text = input("Enter the text to encrypt: ")

encrypted = monoalphabetic_encrypt(plain_text)
print("Encrypted Text:", encrypted)
