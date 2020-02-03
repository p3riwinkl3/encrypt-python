from cryptography.fernet import Fernet
# Storing Keys

def write_keys():
    """
    Generates key and writes it to a file
    """
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key) # The key is type bytes still
    file.close()

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

# write_key()
key = load_key()
message = "some secret message".encode()
f = Fernet(key)

#encrypt the message
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)
print(message)
print(encrypted)
print(decrypted)
