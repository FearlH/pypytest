import numpy as np 
a=np.arange(1,50)
a.shape=(7,7)
print(a)
print(a[...,0:1])
#表示[行操作，列操作]...表示全选

a=np.arange(36).reshape(6,6)
print(a[[1,2,3]])
#a[[哪些行]，[哪些列]]

b=a%2==0
print(b)
print(a[b])

#按照位运算

c=np.sin(a/5)
print(c)
d=c>0
print(d)
print(d&b)

(a>5).any()#只要有一个满足就为真
(a>5).all()#所有满足才为真

f= (a>5)&(a<10)
print(f)
print(a[f])
print(a[[1,2],[3,4]])


#a[[行],[列]]
print(a[range(5),range(1,6)])
print(a[[0,2,5],[2,2,2]])
b=a[3:,::2]
print(b)
c=a[3:,[0,2,5]]#还可以这样切片