#Given the string "label", XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}. 
import sys
#import pycryptodomex
for c in list("label"):
	j=ord(c)
	#k=bin(j)[2:]
	l=j^13
	print(l)
	# print(odr(bin(c)[2:]) ^ 00001101)

