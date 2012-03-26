#!C:/Python27/python.exe -u
# Filename : pow.py

prime =[2,3,5,7,11,13,17,19]		# list of all the prime nos b/w 1 to 20
arr= 8 * [0]    # declaring array of 8 integer as there are 8 prime nos b/w 1 to 20  with value zeros 
ans=1			# to express all the numbers in power of prime nos
				# 1=2^0*3^0*5^0 etc 
				# so for 1 arr[]={0,0,0,0,0,0,0,0}
				# similarly for 2 arr={1,0,0,0,0,0,0,0}
				# for 3 arr={0,1,0,0,0,0,0,0}
				# for 4 arr ={2,0,0,0,0,0,0,0} and so on..

for i in range(1,21):		# range(1,21) so that it can include 20 also in range
	a=i
	j=0
	while(a!=1):
		c=0
		while( a % prime[j] ==0):
				c+=1
				a=a/prime[j]
		if(c>arr[j]):
			arr[j]=c
		j+=1
for i in range(0,8):
	next=pow(prime[i],arr[i])
	ans=ans*next
print ans
