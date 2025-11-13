# Rail Fence Cipher in Python

def encryptRailFence(text, key):
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
    
    # direction flag
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        # reverse the direction when we hit top or bottom
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # place the character
        rail[row][col] = text[i]
        col += 1

        # move up or down
        row += 1 if dir_down else -1

    # collect the encrypted text
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
    
    # mark the zigzag positions
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    # fill the rail with cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == '*') and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1

    # read the text in zigzag
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if (rail[row][col] != '\n'):
            result.append(rail[row][col])
            col += 1

        row += 1 if dir_down else -1

    return "".join(result)


# ---------- MAIN ----------
plain_text = input("Enter message: ").replace(" ", "")
key = int(input("Enter number of rails: "))

cipher_text = encryptRailFence(plain_text, key)
print("\nEncrypted Text:", cipher_text)

decrypted_text = decryptRailFence(cipher_text, key)
print("Decrypted Text:", decrypted_text)
