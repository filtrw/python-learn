"""
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями,
но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать,
какой из паролей служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
"""

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
