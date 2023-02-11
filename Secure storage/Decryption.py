import Encryption as enc
from Cryptodome.Cipher import AES, DES
import base64
from stegano import lsb
from stegano.lsb import generators


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

def rc4(data, key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    result = []
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(chr(ord(char) ^ k))

    return ''.join(result)


decrypted_data = rc4(enc.steganographed_msg, enc.key)
#decrypted_des = decrypt_des(enc.steganographed_msg, enc.des_key)
decrypted_des = decrypt_des(enc.encrypted_des, enc.des_key)
decrypted_aes = decrypt_aes(decrypted_des, enc.aes_key)

print('final Value----',decrypted_aes)
