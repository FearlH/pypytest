import numpy as np
a=np.arange(36).reshape(6,2,3)
b=np.arange(72).reshape(6,4,3)
c=np.append(a,b,axis=1)
print(c)
print(c.shape)

c=np.arange(6).reshape(3,2)
d=np.arange(12).reshape(6,2)
print(c)
print(d)
e=np.concatenate((c,d),axis=0)
print(e)

a=np.arange(36).reshape(6,6)

np.split(a,2,axis=1)

np.split(a,[2,5],axis=1)
#[:2] [2:5] [5:]

help(np.ix_)