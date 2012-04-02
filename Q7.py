import math

MAX =  1000000
to_find = 10001
a = [0] * (MAX+1) 	# an array of size MAX+1 initialized to 0
k = MAX+1
for i in range(0,k):		# initializing array with 1 till MAX+1
	a[i] = 1
	
a[0] = 0
a[1] = 0
n=2 
s= math.sqrt(MAX)
while(n < s): 
	j = n
	marks = 0
	while(j<MAX - n):
					j+=n
					if(a[j] == 1):
						marks+= 1
					a[j] = 0
	if(marks==0): 
		break
	n+= 1
	while(a[n]==0):
		n+= 1
		
cnt = 0
for i in range(0,MAX): 
    if(a[i]==1): 
		cnt+= 1
		if(cnt == to_find): 
			print "The result is ",i

