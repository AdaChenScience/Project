n=float(input('请输入十进制浮点数n:'))
s=''
n1=int(n//1)
n2=n-n1
while(n1>0):
    s+=str(n1%2)
    n1=n1//2
s=s[::-1]+'.'
while n2>0 and len(s)<15:
    n2*=2
    s+=str(int(n2>=1))
    n2-=(n2>=1)
print('转换为二进制为:',s)