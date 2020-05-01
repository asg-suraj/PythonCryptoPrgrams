# this will convert in following way just in reverse (last step to first step)
#message: HELLO
#ascii bytes: [72, 69, 76, 76, 79]
#hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
#base-16: 0x48454c4c4f
#base-10: 310400273487

#take base10 string from user
ctext=int(input('Please give the numeric string: '))
hexvalue=hex(ctext)[2:]
print(hexvalue)
print(bytes.fromhex(hexvalue).decode('utf-8'))

