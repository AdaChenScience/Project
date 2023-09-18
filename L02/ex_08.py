import math
import time
#arctanx级数
estimate=0
k=0
t1 = time.perf_counter()
while abs(math.pi-estimate)>0.00000001:
    if k%2==0:
        estimate+=4/(2*k+1)
    else:
        estimate-=4/(2*k+1)
    k+=1
print('方法一估计值为:%.7f 用时:%.7fs'%(estimate,time.perf_counter()-t1))
#对法一公式进行欧拉变换
estimate=0
k=0
even=1
odd=1
divisor=1
t2 = time.perf_counter()
while abs(math.pi-estimate)>0.00000001:
    estimate+=2*even/odd/divisor
    k+=1
    even*=2*k
    odd*=2*k+1
    divisor*=2
print('方法二估计值为:%.7f 用时:%.7fs'%(estimate,time.perf_counter()-t2))
#BBP公式
estimate=0
k=0
divisor=1
t3 = time.perf_counter()
while abs(math.pi-estimate)>0.00000001:
    estimate+=(4/(8*k+1)-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6)))/divisor
    k+=1
    divisor*=16
print('方法三估计值为:%.7f 用时:%.7fs'%(estimate,time.perf_counter()-t3))