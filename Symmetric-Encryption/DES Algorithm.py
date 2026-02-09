import pyDes

# Create a DES object
# Key must be exactly 8 bytes long
key = pyDes.des(b"8bytekey", pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)

# Message to encrypt
data = input("enter text to encrypt:")

# Encrypt
encrypted_data = key.encrypt(data)
print("Encrypted:", encrypted_data)

# Decrypt
decrypted_data = key.decrypt(encrypted_data)
print("Decrypted:", decrypted_data.decode())
