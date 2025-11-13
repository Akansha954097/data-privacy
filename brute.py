import string
import itertools
def brute_force_cracker(target_password, charset, max_length):
    attempts = 0
    for length in range(1, max_length + 1):

        for guess_tuple in itertools.product(charset, repeat=length):
            attempts += 1
            guess = "".join(guess_tuple)
        
            if guess == target_password:
                print(f"Password cracked! The password is '{guess}'.")
                print(f"Attempts: {attempts}")
                return attempts, guess
    print(f"Password not found after {attempts} attempts.")
    return attempts, None


character_set = string.ascii_letters + string.digits+string.punctuation

password_to_crack = "123"

max_pass_length = 8

print(f"Starting brute-force attack on password '{password_to_crack}'...")
brute_force_cracker(password_to_crack, character_set, max_pass_length)
