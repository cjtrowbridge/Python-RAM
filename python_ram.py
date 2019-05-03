import random
import sys

ram = []*12000
bitlist = []

for x in range(12000):
	bitlist = []
	for i in range(0,8):
		x = str(random.randint(0,1))
		bitlist.append(x)
		
	bitstring = ''.join(bitlist)
	ram.append(bitstring)
	
#read and display the hundredth record
_100th = ram[99]
print('hundredth element: ' + _100th)

#read and display the thousandth record
_1000th = ram[999]
print('thousandth element: ' + _1000th)

#overwrite the 99th and 999th bytes with zeroes
blankByte = [0,0,0,0,0,0,0,0]
ram = replace(ram,blankByte,99)
ram = replace(ram,blankByte,999)

#read and display the hundredth record
_100th = ram[99]
print('overwritten hundredth element: ' + _100th)

#read and display the thousandth record
_1000th = ram[999]
print('overwritten thousandth element: ' + _1000th)

print("Your array can hold a max record of: " , sys.maxsize)
print('\n')

#print alternate elements
i = 0
while(i < len(ram)):
	print(ram[i], end = " ")
	i = i + 2
	
	
		
	
	
