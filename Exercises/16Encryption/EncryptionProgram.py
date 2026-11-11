import random
import string as s

characters = list(" " + s.punctuation + s.digits + s.ascii_letters)
keys = characters.copy()
random.shuffle(keys)

# Encryption
plain_text = input("Enter your message: ")
cipher_text = ""
for letter in plain_text:
    index = characters.index(letter)
    cipher_text += keys[index]

print(f"Original text : {plain_text}")
print(f"Encrypted text : {cipher_text}")

# Decryption
cipher_text = input("Enter your message: ")
plain_text = ""
for letter in cipher_text:
    index = keys.index(letter)
    plain_text += characters[index]

print(f"Original text : {cipher_text}")
print(f"Decrypted text : {plain_text}")
