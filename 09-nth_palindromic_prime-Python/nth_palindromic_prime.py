# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def revNumber(n):
    p=n
    rn = 0
    while(n!=0):
        rm = n%10
        rn = rn*10 + rm
        n = n//10
    return (rn==p)

def isPalindromePrime(n):
    if (isPrime(n)==True) and (revNumber(n)==True):
        return True
    return False


def nthpalidrome(n):
    num=10
    guess=0
    while(n<=guess):
        if isPalindromePrime(n):
            guess+=1
        num+=1
    return num