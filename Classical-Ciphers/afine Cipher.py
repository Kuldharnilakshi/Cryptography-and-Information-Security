def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Modular inverse does not exist")

def encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')
            enc = (a * x + b) % 26
            result += chr(enc + ord('a'))
        else:
            result += char
    return result

def decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    for char in cipher:
        if char.isalpha():
            y = ord(char.lower()) - ord('a')
            dec = (a_inv * (y - b)) % 26
            result += chr(dec + ord('a'))
        else:
            result += char
    return result

# --- Main Program ---
print("Affine Cipher in Python")
choice = input("Do you want to encrypt or decrypt ? (e/d): ").lower()

text = input("Enter the text: ")
a = int(input("Enter key 'a' (must be coprime with 26): "))
b = int(input("Enter key 'b': "))

try:
    if choice == 'e':
        result = encrypt(text, a, b)
        print("Encrypted Text:", result)
    elif choice == 'd':
        result = decrypt(text, a, b)
        print("Decrypted Text:", result)
    else:
        print("Invalid choice! Enter 'e' for encrypt or 'd' for decrypt.")
except ValueError as e:
    print("Error:", e)
