def generate_matrix(keyword):
    keyword = keyword.upper().replace('J', 'I')
    matrix = []
    used = set()

    for char in keyword:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # 'J' is excluded
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += 'X'
    return result

def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt(text, keyword):
    matrix = generate_matrix(keyword)
    prepared = prepare_text(text)
    encrypted = ""

    for i in range(0, len(prepared), 2):
        a = prepared[i]
        b = prepared[i + 1]
        encrypted += encrypt_pair(a, b, matrix)
    return encrypted

# --- User Input and Encryption ---
print("Playfair Cipher - Encryption Only")
text = input("Enter the text to encrypt: ")
keyword = input("Enter the keyword: ")

cipher_text = encrypt(text, keyword)
print("Encrypted Text:", cipher_text)
