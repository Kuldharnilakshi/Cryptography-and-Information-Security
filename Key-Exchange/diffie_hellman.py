# Diffie-Hellman Key Exchange Algorithm in Python

p = int(input("Enter a prime number (p-Alpha): "))
q = int(input("Enter a primitive root (q): "))

XA = int(input("Enter Nilakshi's private key (Pr-A): "))
XB = int(input("Enter Vaishnavi's private key (Pr-B): "))

A = pow(q, XA, p)  
B = pow(q, XB, p)  

print(f"\nNilakshi's Public Key (A): {A}")
print(f"Vaishnavi's Public Key (B): {B}")

secret_A = pow(B, XA, p) 
secret_B = pow(A, XB, p)  

print(f"\nNilakshi's Shared Secret: {secret_A}")
print(f"Vaishnavi's Shared Secret: {secret_B}")


if secret_A == secret_B:
    print("\nKey Exchange Successful! Shared secret established.")
else:
    print("\nKey Exchange Failed!")