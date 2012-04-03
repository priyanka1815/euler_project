# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for i in range(1,26):
    for j in range(1,i+1):
        if(i*(i+j)==500):
            print 2*((i*i*i*i) -(j*j*j*j))*(i*j)
            break;