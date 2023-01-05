#Divisors of a Number

#Brute Force - O(n)

Algorithm:
1.Iterate to the number.
2.Check if the number  is divisible by the iterated nos.
3.Print if yes

def divisors(n):
	for i in range(1,n):
		if n % i == 0:
			print(i)



#Optimised Approach -> O(sqrt(n))
 -> Print the quotient also  and  iterate to the root

Algorithm:
1.Iterate to sqrt(n)
2.check if no is divisible, 
3.Check edge case if i == quootient (in case of perfect square)
4.if Yes, print no and quotient.

def divisor(n):
	for i in range(sqrt(n)):
		if n % i == 0:
			print(i)
			if i != (n//i):
				print(n//i)



#GFG - Sum of all divisors from 1 to n.

def sumOfDivisors(self, n):
	result = 0
    
    for i in range(1,N+1):
        result += (N//i) * i
       
    return result
