from math import gcd

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No modular inverse")
    return x % m

# RSA setup
p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter a public exponent e (1 < e < phi, gcd(e,phi)=1): "))

if gcd(e, phi) != 1:
    print("Invalid e (not coprime with phi).")
else:
    d = modinv(e, phi)
    print(f"Public key: (n={n}, e={e})")
    print(f"Private key: (n={n}, d={d})")

    # Take string input
    plaintext = input("Enter a message to encrypt: ")

    # Convert string to list of ASCII values
    msg_nums = [ord(ch) for ch in plaintext]

    # Encrypt each number
    cipher = [pow(m, e, n) for m in msg_nums]
    print("Encrypted:", cipher)

    # Decrypt each number
    decrypted_nums = [pow(c, d, n) for c in cipher]

    # Convert back to string
    decrypted_text = ''.join(chr(num) for num in decrypted_nums)
    print("Decrypted:", decrypted_text)
