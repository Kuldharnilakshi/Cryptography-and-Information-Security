from Crypto.Cipher import AES
import base64

# AES requires block size = 16
BLOCK_SIZE = 16  

# Padding function (PKCS7)
def pad(data):
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + chr(pad_len) * pad_len

# Unpadding function
def unpad(data):
    pad_len = ord(data[-1])
    return data[:-pad_len]


key = b"thisis16bytekey!"   

cipher = AES.new(key, AES.MODE_ECB)

data = input("Enter text to encrypt: ")

# Encrypt
padded_data = pad(data)
encrypted_data = cipher.encrypt(padded_data.encode())
print("Encrypted:", base64.b64encode(encrypted_data).decode())

# Decrypt
decrypted_data = cipher.decrypt(encrypted_data).decode()
print("Decrypted:", unpad(decrypted_data))

