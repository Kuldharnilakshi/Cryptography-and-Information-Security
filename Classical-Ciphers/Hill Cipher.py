keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k].upper()) - 65
            k += 1

def encrypt(messageVector):
    for i in range(3):
        cipherMatrix[i][0] = 0
        for x in range(3):
            cipherMatrix[i][0] += keyMatrix[i][x] * messageVector[x][0]
        cipherMatrix[i][0] = cipherMatrix[i][0] % 26

def HillCipher(message, key):
    getKeyMatrix(key)

    for i in range(3):
        messageVector[i][0] = ord(message[i].upper()) - 65

    encrypt(messageVector)

    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    print("Ciphertext:", "".join(CipherText))

def main():
    print("Hill Cipher Encryption")

    message = input("Enter 3-letter plain-text: ")
    key = input("Enter 9-letter Key: ")

    if len(message) != 3 or len(key) != 9:
        print("Invalid input! Message must be 3 letters and key must be 9 letters.")
        return

    HillCipher(message, key)

if __name__ == "__main__":
    main()
