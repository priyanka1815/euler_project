#Find the sum of all the primes below two million.
import math

def isPrime(num):
	if(num==2):
		return True
	else:
		k = int(math.sqrt(num))+1
		for i in range(2,k):
			if(num % i == 0):
				return False
	return True
		
sum = 0
num = 2000000
for i in xrange(2,num):
	if(isPrime(i)):
		print "\nprime= ",i
		sum += i

print "\nsum=",sum