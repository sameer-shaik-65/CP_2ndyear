# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def Happynum(n):
    sum = 0
    while(n!=0):
        sum += (n%10)**2
        n//=10
    if sum == 1:
        return True
    elif sum<10:
        return False
    else:
        return Happynum(sum)
def nth_happy_number(n):
    f = 1
    g = 0
    while(f<=abs(n)):
        g+=1
        if(Happynum(g)):
            f+=1
    return g