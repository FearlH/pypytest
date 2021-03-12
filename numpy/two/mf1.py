import numpy as np
A=np.arange(3,15).reshape(3,4)
print(A)
print(A[2])
print(A[:2,1])
for x in A:#默认按照行来迭代
    print(x)

for x in A.T:#转置
    print(x)
for x in range(A.shape[0]):
    print(A[...,x:x+1])
    print()

B=A.flat#转化为一行返回一个迭代器
B=A.flatten()#返回一个数组把A映射到一行里面
print(B)
for x in B:
    print(x)



A=np.array([[[1,1,1],[3,3,3],[5,5,5]],[[4,5,6],[3,3,3],[5,5,5]],[[7,8,9],[3,3,3],[5,5,5]]])
B=np.array([[[2,2,2],[4,4,4],[6,6,6]]])
print(A)
C=np.append(A,B,axis=0)#在0维度上面把B落上去
print(C)
print(B)
print(B.shape)
print(C.shape)

#stack 是按照新的轴连接一个数组
'''
A B 都是(4,3) 那么按照 axis=1/2/3进行连接就会得到
(2,4,3)  (4,2,3)  (4,3,2)这几个
'''
A=np.array([1,1,1])
print(A[np.newaxis,:])
print(A[:,np.newaxis])
B=np.array([2,2,2])
C=np.stack((A,B),axis=0)#新轴是行
print(C)
D=np.stack((A,B),axis=1)#新轴是列
print(D)
E=np.hstack((A,B))
print(E.shape)

G=np.vstack((A,B))
print(G.shape)

F=np.array([[1,1,1],[2,2,2]])
print(F)
print(F[:,:,np.newaxis])#在一个方向上面加了一个维度
print(F[:,np.newaxis,:])
print(F[np.newaxis,:,:])

A=[[1,2,3],[4,5,6]]
B=[[7,8,9],[14,15,16]]
print(np.concatenate((A,B),axis=1))#在哪一个维度合并
print(np.append(A,B,axis=1))


A=np.arange(12).reshape(3,4)
print(A)
print(np.split(A,3,axis=0))
print(np.split(A,2,axis=1))


#不等量分割
print(np.array_split(A,3,axis=1))


#赋值

A=np.array([1,2,3,4])
B=A
C=B#它们都是A，就是把B指向A指向的东西，C也指向了
A[0]=11
print(C)

print(B is A)#判断是不是指向了同一个东西

#浅拷贝

D=A.copy()

print(D is A)

E=A[:]
print(E is A)

