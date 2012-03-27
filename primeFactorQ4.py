#!C:/Python27/python.exe -u
# Filename : primeFactorQ4.py

# question- Largest Prime factor of 600851475143

import math

n = 600851475143
sq = int(math.floor(math.sqrt(n)))		# taking sqrt of the number
for i in range(sq,1,-1):
	if(n%i==0):			# checking if i is factor of n
		k = (i/2)
		for j in range(k,1,-1):		# if i is factor then checking if it is prime or not
			if(i % j == 0):
				break
		else:
			max_prime= i
			break

print "\nLargest Prime factor of 600851475143 is :",i