#program to convert given hex string to plain text
import codecs


hexString= input('Enter hex string')
#hexString = hexString[2:]
#p=bytes.fromhex(hexString[2:]).decode('utf-8')
hexString=hexString.decode().hex()
#print(p)
#

