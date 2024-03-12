#Calculate the greatest common divisor of a and b.
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
m,n=input('请输入两个正整数(以空格隔开):').split(' ')
print('这两个数的最大公约数为:',gcd(int(m),int(n)))