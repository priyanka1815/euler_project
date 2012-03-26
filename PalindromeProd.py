#!C:/Python27/python.exe -u
# Filename : PalindromeProd.py

def palindrome(num):		# defining function palindrome
	y = 0
	a = num
	i = 0
	while(a):			# reversing the number
		u = a%10
		a = a/10
		y = y*10+u
		i += 1
	if(y==num):
		return 1
	else:
		return 0		

x=999
y=999
flag=0
ans=1*1
posi=0
posj=0
    
for i in range(x,101,-1):		# decrementing for loop with -1 therefore 3 parameter in range()
    for j in range(i,101,-1):
			if(palindrome(i*j)):
				if(ans<(i*j)):
					ans=i*j
					posi=i
					posj=j
					
print posi,"*",posj,"   =  ",ans