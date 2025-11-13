import random
import string

def generate_password(dictionary_file, num_words=4, separator='-', add_numbers=True, add_symbols=True):
    try:
        with open(dictionary_file, 'r') as f:
            words = [line.strip().lower() for line in f if line.strip().isalpha()]
    except FileNotFoundError:
        print(f"Error: File '{dictionary_file}' not found.")
        return None

    if len(words) < num_words:
        print("Error: Not enough words in the dictionary file.")
        return None

    chosen_words = random.sample(words, num_words)

    password = separator.join(chosen_words)

    if add_numbers:
        password += str(random.randint(0, 99))

    if add_symbols:
        password += random.choice(string.punctuation)

    return password



    
dict_file = "dictionary_file.txt"  

password = generate_password(dict_file, num_words=4)
if password:
    print("Generated password:", password)
