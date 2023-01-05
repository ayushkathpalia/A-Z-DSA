# Find GCD/HCF of two numbers 


#Brute Force -> O(n),O(1)

Algorithm:
1.Find min of the nos.
2.Traverse from 1 to min no.
3.Find the maximum value of i which divides both a and b.

def GCD(n1,n2):
	x = min(n1,n2)
	res = 0
	for i in range(1,x):
		if n1 % i == 0 and n2 % i == 0:
			res = i

	return res



#Using Euclidean's Theorem -> O(log min(a,b)),O(1)

gcd(a,b) = gcd(b,a%b)

Algorithm:
1.Recusively call gcd(b,a%b) function till base condition
2.Base condition is b = 0 
3.When base condition hits, return a


def GCD(a,b):
	if b == 0:
		return a
	return GCD(b,a%b)



 
 GFG : LCM & GCD

def lcmAndGcd(self, A , B):
    # code here 
    gcd = self.gcd(A,B)
    lcm = (A*B)//gcd
    return [lcm,gcd]

def gcd(self,A,B):
    if B == 0:
        return abs(A)
    return self.gcd(B,A%B)