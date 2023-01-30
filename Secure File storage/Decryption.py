from Cryptodome.Cipher import AES
import Encryption
file_in = open("encryptedfile.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
key=Encryption.key
#the person decrypting the message will need access to the key
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)
print(data.decode('UTF-8'))