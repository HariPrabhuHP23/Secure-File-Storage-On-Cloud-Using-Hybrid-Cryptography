from Cryptodome.Cipher import AES, DES
import base64

def encrypt_aes(secret_message, key):
    # pad the secret message so that its length is a multiple of 16
    secret_message = secret_message + ((16 - len(secret_message) % 16) * '{')
    secret_message = secret_message.encode('utf-8')
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_message = cipher.encrypt(secret_message)
    return base64.b64encode(encrypted_message).decode('utf-8')

def encrypt_des(secret_message, key):
    # pad the secret message so that its length is a multiple of 8
    secret_message = secret_message + ((8 - len(secret_message) % 8) * '{')
    secret_message = secret_message.encode('utf-8')
    key = key.encode('utf-8')
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_message = cipher.encrypt(secret_message)
    return base64.b64encode(encrypted_message).decode('utf-8')


aes_key = 'abcdefghijklmnop' #  16-byte key
des_key = 'abcdefgh' #  8-byte key
secret_message = 'Hello, World!'

encrypted_aes = encrypt_aes(secret_message, aes_key)
encrypted_des = encrypt_des(encrypted_aes, des_key)
#print(encrypted_des)