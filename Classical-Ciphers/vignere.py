def vigenere_encrypt(plain_text, keyword):
    encrypted = ""
    keyword_repeat = ""
    while len(keyword_repeat) < len(plain_text):
        keyword_repeat += keyword
    keyword_repeat = keyword_repeat[:len(plain_text)]

    for p_char, k_char in zip(plain_text, keyword_repeat):
        if p_char.isalpha():
            p_index = ord(p_char) - ord('a')
            k_index = ord(k_char) - ord('a')
            enc_index = (p_index + k_index) % 26
            encrypted += chr(enc_index + ord('a'))
        else:
            encrypted += p_char

    return encrypted

# --- User Input and Encryption ---
print("Vigenere Cipher Encryption Only")
text = input("Enter the text to encrypt: ")
keyword = input("Enter the keyword: ")

encrypted_text = vigenere_encrypt(text, keyword)
print("Encrypted Text:", encrypted_text)
