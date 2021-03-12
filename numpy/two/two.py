import numpy as np
a=np.array([[1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19]])
b=np.tile(a,(3,9))#3*9矩阵每个里面用a填充，还是2维
print(b)
b
print(b.shape)

c=np.arange(6).reshape(3,2,1)
print(c)

v=np.tile(c,(2,2))
print(v)
print(v.shape)