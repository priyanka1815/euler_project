#Find the sum of all the primes below two million.
# using SIEVE ALGORITHM

import math

sieve_prime_array = [1] * 2000000  # creating an array initialized with 1 of range 2 million

def mark_composite(sieve_prime_array,num):	#marking the composite no in array as 0
	start = num*2
	end = len(sieve_prime_array)
	for i in xrange(start,end,num):
		sieve_prime_array[i]=0


size = int(math.sqrt(len(sieve_prime_array))) +1	
for i in xrange(2,size):
	if(sieve_prime_array[i]):
		mark_composite(sieve_prime_array,i)

sum =0
for j in xrange(2,len(sieve_prime_array)):	# adding the index of no in array which are 1
	if(sieve_prime_array[j]):
		sum += j

print "sum=", sum

