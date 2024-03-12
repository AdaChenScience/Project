import numpy as np
import random
import math
num_list=np.random.random(10000000)+2
avg=sum([x**2+4*x*math.sin(x) for x in num_list])/len(num_list)
print('该定积分值约为:%.5f'%(avg*1))