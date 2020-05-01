
from pwn import * # pip install pwntools
import json
import base64
import codecs
import random
from Crypto.Util.number import bytes_to_long, long_to_bytes
#Decoding somme common types with this code 100 times
r = remote('socket.cryptohack.org', 13377, level = 'debug')
for x in range(1,102): #1-101 100 levels are completed and 102 will send answer

    def json_recv():
        line = r.recvline()
        return json.loads(line.decode())
        

    def json_send(hsh):
        request = json.dumps(hsh).encode()
        r.sendline(request)


    received = json_recv()
    #print("Received type: ")
    #print(received["type"])
    encoding=received["type"]
    #print("Received encoded value: ")
    #print(received["encoded"])
    eString=received["encoded"]

    if encoding == "base64":
        decoded  = str(base64.b64decode(eString), "utf-8")
    elif encoding == "hex":
        decoded = str(bytes.fromhex(eString).decode('utf-8'))
    elif encoding == "rot13":
        decoded = codecs.encode(eString, 'rot_13') #encoding second time is again decryption
    elif encoding == "bigint":
        decoded = bytes.fromhex(eString[2:]).decode('utf-8')
    elif encoding == "utf-8":
        lo=""
        for b in eString:
            lo=lo+chr(b)
        decoded=lo


    to_send = {
        "decoded": decoded
    }
    json_send(to_send)
    print('Level '+str(x)+'is complete')
