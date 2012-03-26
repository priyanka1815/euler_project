#!C:/Python27/python.exe -u
# Filename : sumNatural.py

sum=0
for i in range(1,1000):
	if( i%3 ==0 or i%5 ==0):
					sum = sum+ i
		
print '''The sum of natural numbers divisile'
by 3 and 5 is ''',sum
