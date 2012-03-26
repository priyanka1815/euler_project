#!C:/Python27/python.exe -u
# Filename : sumFibbo.py

last= 0
current = 1
sum = 0
total = 0
while current < 4000000:
		sum = last + current
		last = current
		current = sum
	
		if sum >= 4000000:
			break
		else:
			if sum % 2 == 0:
				total += sum
else: print "done"			
print(total)