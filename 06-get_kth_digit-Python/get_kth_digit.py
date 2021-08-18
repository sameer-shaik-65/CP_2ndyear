# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
    
  l=[]
  digit=abs(digit)
  while(digit):
    l.append(digit%10)
    digit=digit//10
  #print(l)
  if len(l)<=k:
    return 0

  return l[k]
