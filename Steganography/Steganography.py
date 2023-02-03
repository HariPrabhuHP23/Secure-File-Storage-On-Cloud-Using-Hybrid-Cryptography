from stegano import lsb
from stegano.lsb import generators

message='Phone la pesatha da p***'
hide=lsb.hide('pexels-alex-urezkov-10024233.png',message,generators.eratosthenes())
hide.save("Hidden.png")
##decrypt
unhide=lsb.reveal("Hidden.png",generators.eratosthenes())
print(unhide)

'''
from stegano import lsb

secret = lsb.hide("pexels-alex-urezkov-10024233.png",'Hi da ')
secret.save("output_image.png")

## Decrypt

data=lsb.reveal('output_image.png')
print(data)

'''