import numpy as np
a=np.arange(30).reshape(2,3,5)
print(a.shape[0])#在哪个维度上面的个数
print(np.zeros(10))#一维度的0

X=np.arange(36).reshape(12,3)
y=np.arange(12).reshape(12)
print(X)
print(zip(X,y))
for x,y in zip(X,y):
    print(x,y)