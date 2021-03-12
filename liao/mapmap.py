#map和reduce
#map 就是把函数作用到每个list的元素上面，然后给出输出值
#输出值不是一个list 是一个Iterator，可迭代的东西，可以转化为list
#对于其他的Itreator也是成立的
from functools import reduce

def f(x):
    return x*x

L=map(f,[1,2,3,4,5,6,7,8,9])
for x in L:
    print(x)

def f1(x1,x2):
    return 10*x1+x2
#reduce函数，接收的是二元函数
#[x1,x2,x3,x4,x5]把二元函数作用在前两个值上面f(x1,x2)，然后再得到输出Y
#在作用f1(Y,x3)
#最后得到一个结果

P=reduce(f1,[1,2,3,4,5,6,7,8,9])
print(P)


#格式化
print(len([1,2,3]))
print(list(range(10)))#只到9
def f3(B):
    return[B[n][i].upper() if i==0 else B[n][i].lower() for n in range(len(B)) for i in range(len(B[n]))]
L=map(f3,["alIce","Bob","tony"])
for name in L:
    print(name)


def f4(L):
    s=""
    for i in range(len(L)):
        if i==0:
            c=L[i].upper()
        else:
            c=L[i].lower()
        s+=c
    return s
F =map(f4,["alIce","Bob","tony"])#在函数定义的时候就不需要再进行一次循环了
#是 对于每一个进行操作，相当于迭代了每一个了
for name in F:
    print(name)

L=["alIce","Bob","tony"]
s=""
for n in range(len(L)):
    for i in range(len(L[n])):
        if i==0:
            c=L[n][i].upper()
        else:
            c=L[n][i].lower()
        s+=c
    print(s)

def prod(x1,x2):
    return x1*x2

print(reduce(prod,[1,2,3,4,5,6,7,8,9]))

def c2i(x):
    dictt={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':"."}
    def f1(x):
        return dictt[x]
    def f2(x1,x2):
        if(x2=="."):
            return x1
        else:
            flag=True
            return x1*10+x2
    for i in range(len(x)):
        if x[i]==".":
            break
    L=map(f1,x)
    P=reduce(f2,L)
    for i in range(len(x)-i-1):
        P/=10
    return P
print(c2i("123.456"))



def f2(x1,x2):
        if(x2=="."):
            return x1
        else:
            return x1*10+x2
print(reduce(f2,[1,2,3,".",4,5,6]))

    
    
