x=float(input('请输入x:'))
y=float(input('请输入y:'))
z=float(input('请输入z:'))
l=[x,y,z]
l.sort()
print('这三个数从小到大依次为:',*l)