import Encryption as enc
from Cryptodome.Cipher import AES,DES
import base64

def decrypt_des(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message.encode('utf-8'))
    key = key.encode('utf-8')
    cipher = DES.new(key, DES.MODE_ECB)
    secret_message = cipher.decrypt(encrypted_message)
    # remove the padding
    secret_message = secret_message.decode('utf-8').rstrip("{")
    return secret_message

def decrypt_aes(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message.encode('utf-8'))
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    secret_message = cipher.decrypt(encrypted_message)
    # remove the padding
    secret_message = secret_message.decode('utf-8').rstrip("{")
    return secret_message

decrypted_des = decrypt_des(enc.encrypted_des,enc.des_key)
decrypted_aes = decrypt_aes(decrypted_des,enc.aes_key)
print(decrypted_aes)
