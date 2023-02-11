from stegano import lsb
from stegano.lsb import generators

message='Hi there !!!!!'
hide=lsb.hide('pexels-alex-urezkov-10024233.png',message,generators.eratosthenes())
hide.save("Hidden.png")
##decrypt
unhide=lsb.reveal("Hidden.png",generators.eratosthenes())
print(unhide)

