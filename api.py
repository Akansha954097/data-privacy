import requests
import hashlib

password_file = "password.txt"

try:
    with open(password_file, 'r') as f:
        for line in f:
            username,password = line.strip().split(',',1)
            sha1_obj = hashlib.sha1(password.encode()).hexdigest().upper()
            prefix,suffix = sha1_obj[:5],sha1_obj[5:]
            

        try:
            response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
            for res_line in response.text.splitlines():
                res_suffix,count = res_line.split(':')
                if res_suffix == suffix:
                    print(f'Your password has been leaked for {count} no. of times!')
                    break
            else:
                print("Your password is safe!")
        except requests.RequestException:
            print("A Problem has occurred!")


        
        
except FileNotFoundError:
    print("No file found!")
