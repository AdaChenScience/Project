import numpy as np
import matplotlib.pyplot as plt

sample=np.random.normal(0,1,size=10000)
# plt.hist(sample,bins=15)

fig,ax = plt.subplots()
n,bins_num,pat = ax.hist(sample,bins=20,alpha=0.75)
ax.plot(bins_num[:-1]+0.2,n,marker = 'o',color="yellowgreen",linestyle="--")

plt.title("normal distribution")
plt.xlabel("data")
plt.ylabel("frequency")
plt.show()