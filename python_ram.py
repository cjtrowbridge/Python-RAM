import random
inport sys

array = []*12000
bitlist = []

for x in range(12000):
	bitlist = []
	for i in range(0,8):
		x = str(random.randint(0,1))
		bitlist.append(x)
		
	bitstring = ''.join(bitlist)
	array.append(bitstring)
	
#read and display the hundredth record
_100th = array[99]
print('hundredth element: ' + _100th)

#read and display the thousandth record
_1000th = array[999]
print('thousandth element: ' + _1000th)

print("Your array can hold a max record of: " , sys.maxsize)
print('\n')
