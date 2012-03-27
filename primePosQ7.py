#!C:/Python27/python.exe -u
# Filename : primePosQ7.py

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# 1 is not a prime.
# All primes except 2 are odd.
# All primes greater than 3 can be written in the form 6k+/-1.
# Any number n can have only one prime factor greater than sqrt(n) .
# The consequence for primality testing of a number n is: if we cannot find a number f less than
# or equal sqrt(n) that divides n then n is prime: the only primefactor of n is n itself

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




# faster method

o find all the prime numbers less than or equal to a given integer n by Eratosthenes’ method:
Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
Initially, let p equal 2, the first prime number.
Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list. These numbers will be 2p, 3p, 4p, etc.; note that some of them may have already been marked.
Find the first number greater than p in the list that is not marked; let p now equal this number (which is the next prime).
If p is less than n, repeat from step 3. Otherwise, stop.



#include <iostream>
#include <cmath>

using namespace std;

//I don't know how large the munber will up to.
//Assign a large one: 1 million
#define LARGE_NUMBER 1000000
#define NUMBER 10001

int main() {
        //After checked, 0 means prime, and 1 means component.
        int a[LARGE_NUMBER+1] = {0};
        for(int i=0;i<LARGE_NUMBER+1;++i) a[i] = 1;
        a[0] = 0; a[1] = 0;
        int n=2, s=sqrt(LARGE_NUMBER);
        while(n < s) {
                //cout << n << " ";
                int j = n;
                int marks = 0;

                while(j<LARGE_NUMBER - n) {
                        j+=n;
                        if(a[j] == 1) {
                                marks++;
                        }
                        a[j] = 0;
                }
                if(marks==0) {
                        break;
                }
                while(a[++n] == 0); //get next prime
        }
        int cnt = 0;
        for(int i=0;i<=LARGE_NUMBER; ++i) {
                if(a[i]==1) {
                        if(++cnt == NUMBER) {
                                cout << "The result is " << i << endl;
                        }
                }
        }
        cout << "Additionally, there are " << cnt << " prime numbers below 1 million." << endl;
}