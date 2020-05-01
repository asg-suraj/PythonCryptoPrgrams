#to Base64 from hex value
import base64
import codecs
hexString= input('Enter hex string')
b64 = codecs.encode(codecs.decode(hexString, 'hex'), 'base64').decode()
print(b64);

