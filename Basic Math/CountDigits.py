#CountDigits


O(n),O(1)
def count_digits(n):
   count=0
   x=n
   while( x != 0 ):
           x//=10
           count+=1
   return count


#GFG
# Given a number N. Count the number of digits in N which evenly divides N.
# Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.

def evenlyDivides (self, N):
    # code here
    count = 0
    tmp = N
    while tmp :
        rem = tmp % 10
        if rem != 0:
            if N % rem == 0:
                count+=1
        tmp = tmp//10
    return count
