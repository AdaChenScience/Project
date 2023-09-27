import math
n=int(input('请输入正整数n:'))
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
print(isPrime(n))