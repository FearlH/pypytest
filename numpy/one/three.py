import numpy as np
a=np.arange(20)
b=a[1:19:2]
b


c=[[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]]
c=np.array(c)
print(c.shape)
d=c[1:]
d
e=c[...,1:]
e

 
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素