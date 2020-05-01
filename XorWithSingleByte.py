#xor With single byte
#the input is hex String
import codecs
import base64
import binascii

hexString= input('Enter hex string')



encoded = binascii.unhexlify(hexString)
print(encoded)
for xor_key in range(256):
    decoded = ''.join(chr(b ^ xor_key) for b in encoded)
    if decoded.isprintable():
        print(xor_key, decoded)


#import binascii   #Solution
#string = binascii.unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
#l = [c for c in string]
#for i in range(256):
#     f = [chr(n^i) for n in l]
#     a = "".join(f)
#     if a.startswith("crypto"):
#             print(a)
