from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()

message = "my deep dark secret".encode()

f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)

decrypted = f.decrypt(encrypted)

print(decrypted)