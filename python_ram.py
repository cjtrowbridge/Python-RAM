import random
import sys
import string

ram = []*12000
bitlist = []

def displayRecords(prepend =''):
	hundredth  = ''.join(str(v) for v in ram[99])
	thousandth = ''.join(str(v) for v in ram[999])
	print(prepend + 'hundredth element: '  + hundredth)
	print(prepend + 'thousandth element: ' + thousandth)

def blankOut(byteNumber):
	ram[byteNumber]='00000000'

for x in range(12000):
	bitlist = []
	for i in range(0,8):
		x = str(random.randint(0,1))
		bitlist.append(x)
	bitstring = ''.join(bitlist)
	ram.append(bitstring)
	
displayRecords()

#overwrite the 99th and 999th bytes with zeroes
blankOut(99)
blankOut(999)

displayRecords('overwritten ')
print('The array can hold a max of 1500 8-byte words for a total size of 12,000 bits.\n')

#print alternate elements
i = 1
while(i < len(ram)):
	print(str(i)+":"+str(ram[i]) + " "),
	i = i + 2