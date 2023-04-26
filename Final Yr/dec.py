from Cryptodome.Cipher import AES, DES, ARC4
import base64
from stegano import lsb
from stegano.lsb import generators
import os

rc4_key = 'secret_key'
des_key = 'abcdefgh'
aes_key = '0123456789ABCDEF'

def decrypt_aes(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message.encode('utf-8'))
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    # unpad the message after decryption
    decrypted_message = cipher.decrypt(encrypted_message).rstrip(b"\0")
    return decrypted_message.decode('utf-8')


def decrypt_des(encrypted_message, key):
    encrypted_message = base64.b64decode(encrypted_message.encode('utf-8'))
    key = key.encode('utf-8')
    cipher = DES.new(key, DES.MODE_ECB)
    # unpad the message after decryption
    decrypted_message = cipher.decrypt(encrypted_message).rstrip(b"\0")
    return decrypted_message.decode('utf-8')

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

def main(data):
    decrypted_RC4= rc4(data, rc4_key)
    decrypted_des = decrypt_des(decrypted_RC4, des_key)
    decrypted_aes = decrypt_aes(decrypted_des, aes_key)
    return decrypted_aes
