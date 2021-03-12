import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print(a)
print(a.shape)
a=np.array([1,2,3,4,5,6,7,8,9])
c=np.array(np.arange(9))#0-8
c
b=np.eye(5)
print(b.shape)
print(b.ndim)
a
b
b[1]#读一行
b[:,2]#一列
#每个对应元素的计算
d=a+c
d
d=a-c
d
d=a*c
d
d=a/c
d
d=a**c
d
dt=np.dtype([("name","S20"),("age","i4")])#类似于每个数据存放一个结构体
arr=np.array([("dlrb",20),("glnz",19)],dtype=dt)
print(arr["name"])
print(arr["age"])
print(arr)
print(arr.shape)


