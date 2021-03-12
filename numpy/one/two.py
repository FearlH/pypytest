import numpy as np
a=np.array(np.arange(10))
print(a)
b=a.reshape(2,5)#a保持原样,拷贝
b[1,4]=20#b改变了a也变
print(b)
print(a)
a.shape=(3,3)
a


n=np.empty([3,2],dtype=np.int)
c=np.zeros([2,2],dtype=np.float)
c
d=np.ones([4,5],dtype=np.int)
d

it=(x*x for x in range(10))

e=np.fromiter(it,dtype=np.long)
e

e=np.arange(start=1,stop=10,step=2,dtype=np.float)
e


f=np.linspace(1,12,2,endpoint=False)#等差数列
f


g=np.logspace(start=3,stop=9,num=20,base=2)#从base的3次方到base的9次方生成等比数列num个
