from Cryptodome.Cipher import DES,AES
import base64
from stegano import lsb
from stegano.lsb import generators
import os

rc4_key = 'secret_key'
des_key = 'abcdefgh'
aes_key = '0123456789ABCDEF'

def encrypt_aes(message, key):
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    # pad the message before encryption
    padded_message = message.encode('utf-8') + b"\0" * (AES.block_size - len(message) % AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return base64.b64encode(encrypted_message).decode('utf-8')



def encrypt_des(message, key):
    key = key.encode('utf-8')
    cipher = DES.new(key, DES.MODE_ECB)
    # pad the message before encryption
    padded_message = message.encode('utf-8') + b"\0" * (DES.block_size - len(message) % DES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return base64.b64encode(encrypted_message).decode('utf-8')

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

def main(key):
    message = key

    encrypted_aes= encrypt_aes(message, aes_key)


    encrypted_des = encrypt_des(encrypted_aes, des_key)

    encrypted_rc4 = rc4(encrypted_des, rc4_key)


    #basepath = os.path.dirname(__file__)
    #hide = lsb.hide('Checking.png',encrypted_rc4, generators.eratosthenes())
    #imagepath1 = os.path.join(basepath, 'steganographed_' + "Checking.png")
    #hide.save(imagepath1)

    return encrypted_rc4

