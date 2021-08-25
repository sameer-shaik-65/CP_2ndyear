# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def isPrime(n):
    n = int(n)
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
 
def getSum(n):
 
    sum = 0
    while (n != 0):
        sum = sum + n % 10
        n = n / 10
    return sum

def isAdditivePrime(n):
    if (not isPrime(n)):
        return False
    return isPrime(getSum(n))
    
print(isAdditivePrime(290))