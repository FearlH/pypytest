import numpy as np
a=np.array([[1,2,3],[4,5,6]])
a

#改变数据的类别

b=a.astype(np.float)#a不会变
print(b)
print(a)
b=np.arange(1,10,0.1)
print(b)

c=np.sin(b)
print(c)

print(b<4)

A=np.array([True,False])
B=np.array([False,True])

print(np.logical_and(A,B))



c=np.arange(30)
c.reshape(5,6)#返回的是一个5*6的copy，原来的维数不变
c.shape=(5,6)
print(c)
d=c.reshape(-1,2)#用一个负数表示不指定,就是只有2列
#30个元素分成2列
c.shape=(-1,2)
print(d)

c=np.arange(30)
c.reshape(5,6)
f=c.reshape(5,3,2)
print(f)

g=np.sum(f,axis=0)#按照第一个维度+
print(g)

l=np.sum(f,axis=1)#按照第二个维度+
print(l)
print(l.shape)
l=np.sum(f,axis=1,keepdims=True)#按照第二个维度+
#Ture保持维度不变
print(l)
print(l.shape)

a=np.empty_like(f)#形状一样看怎么填充
print(a)


a1=range(10)
a2=range(10,20)
print(a1,a2,zip())
print(a1,a2,zip())

A=np.arange(20).reshape(4,5)
B=np.arange(4)
C=zip(A,B)

for x,y in C:
    print(x,"+",y)

