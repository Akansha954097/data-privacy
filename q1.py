# Caesar Cipher in Python

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():  # uppercase letters
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():  # lowercase letters
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char  # keep spaces/punctuation unchanged
    return result


def decrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            result += char
    return result


# ---------- MAIN ----------
plaintext = input("Enter message: ")
key = int(input("Enter key (number): "))

encrypted = encrypt(plaintext, key)
print("\nEncrypted Text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Text:", decrypted)
