from os import path
from simplecrypt import decrypt, DecryptionException

password_file_path = path.join(".", "file_samples", "passwords.txt")
password_list = open(password_file_path).readlines()

important_information_file_path = path.join(".", "file_samples", "encrypted.bin")

with open(important_information_file_path, "rb") as inp:
    encrypted = inp.read()

for password in password_list:
    try:
        print(
            f' Password = {password.strip()} \n encrypted data = {decrypt(password.strip(), encrypted).decode("utf-8")}')
    except DecryptionException as e:
        print(e)
