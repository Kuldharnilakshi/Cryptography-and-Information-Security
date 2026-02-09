import hashlib

# Take input from user
text = input("Enter text: ")

# Encode and create MD5 hash
md5_hash = hashlib.md5(text.encode())

# Print hexadecimal digest
print("MD5 Hash:", md5_hash.hexdigest())
