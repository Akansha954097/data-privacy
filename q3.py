import hashlib

def hash_password(password):
    # Encode the password into bytes, then create SHA-256 hash
    hashed = hashlib.sha256(password.encode())
    # Return hexadecimal representation
    return hashed.hexdigest()

# ---------- MAIN ----------
password = input("Enter your password: ")
hashed_password = hash_password(password)

print("\nSHA-256 Hashed Password:")
print(hashed_password)
