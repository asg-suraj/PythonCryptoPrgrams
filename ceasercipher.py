import sys
import pycryptodomex
ch='s';
while(ch=='s'):
    print('Welcome to ceaser cipher encryptor & Decryptor')
    
    choice = int(input('Enter choice 1 for Encrypt 2 for decrypt:'))
    if(choice==1):
        key=int(input('please Enter the Shift key'))
        ptext=input('Enter the plaintext')
        ctext=''
        for char in ptext:
            if (char == ' '):
                ctext=ctext+char
            elif (char.isupper()):  #isupper() checks for upper case character
                cext=ctext+chr((ord(char)-65+key)%26+65) #ord(char) will genrate ascii value of charachter
            else:
                ctext=ctext+chr((ord(char)-97+key)%26+97)
        print(ctext)
    else:
        key=int(input('please Enter the Shift key'))
        ctext=input('Enter the Ciphertext')
        ptext=''
        for char in ctext:
            if (char == ' '):
                ptext=ptext+char
            elif (char.isupper()):  #isupper() checks for upper case character
                pext=ptext+chr((ord(char)-65-key)%26+65)  #chr(value) returns Character of that value
            else:
                ptext=ptext+chr((ord(char)-97-key)%26+97)
        print(ptext)
    ch=input('press s to start again else press any other key:')   

