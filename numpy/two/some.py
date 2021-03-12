import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)
c=a+b
print(c)

d_dot=np.dot(a,b)#矩阵
d=a*b#逐个相乘
print(d_dot)
print(d)

a=np.random.random((2,4))#2行4列0-1
print(a)
print(np.sum(a,axis=0))#asix表示被压缩的那维度，被压缩的是哪一个就表示对于哪一个进行运算
print(np.min(a,axis=0))
print(np.min(a,axis=1))
print(np.max(a,axis=1))
a=np.array([[1,2,9,7],[4,5,6,4],[7,8,3,1]])
print(a)


A=np.arange(20,0,-1).reshape(4,5)
B=np.arange(40).reshape(5,2,4)
print(np.max(B,axis=0))
print(B)
print(A)
print(np.argmax(A,axis=0))#按照哪个维度被压缩了进行计算
print(np.argmin(A))#最大最小值所在的矩阵的位置
print(np.mean(A,axis=0))#平均值
print(np.median(A))#中位数
print(np.cumsum(A,axis=1))
a=np.arange(14).reshape(2,7)
print(np.cumsum(a,axis=1))#相当于reduce但是每一步都输出
#得到7列，每一列的值都是对于被压缩之后取值的相应的运算结果
print(np.diff(a))#两两相减
print(np.cumsum(np.arange(7)))
print(np.nonzero(a))#得到非0数字的位置索引


A[0][1]=30
print(np.sort(A))
print(A)

print(np.transpose(A))#都是转置
print(A.T)#都是转置

print(np.clip(A,5,9))#把范围限制在5,9范围之内




