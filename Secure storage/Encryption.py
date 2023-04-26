from stegano import lsb
from stegano.lsb import generators
from Cryptodome.Cipher import AES, DES
import base64


#data =input("Enter the key:-")
key = "key"
aes_key = 'abcdefghijklmnop' #  16-byte key
des_key = 'abcdefgh' #  8-byte key

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



def main():
    encrypted_aes = encrypt_aes(data, aes_key)
    encrypted_des = encrypt_des(encrypted_aes, des_key)
    encrypted_data = rc4(encrypted_des, key)
    print("RC4",encrypted_data)
    #print("Encrypt KEY ---",encrypted_des)
    ###Steganography

    hide=lsb.hide('pexels-alex-urezkov-10024233.png',encrypted_data,generators.eratosthenes())
    hide.save("Hidden.png")
    steganographed_msg=lsb.reveal("Hidden.png",generators.eratosthenes())
    print('stegno--',steganographed_msg)
