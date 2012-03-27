#!C:/Python27/python.exe -u
# Filename : primePosQ7.py
# What is the 10001st prime number?


# not working

import math

count = 0
i=3
while(count<1001):
	if(i%2==0):
		print "\nsorry",i
		continue
	else:
		while(True):
			k = (i/2)
			for j in range(k,1,-1):	
				if(i % j == 0):
					print "\nsorry not prime",i
					continue
				else:
					count+= 1
	if(count == 1001):
		break
	i+= 1

print "10001st prime number is :", i
