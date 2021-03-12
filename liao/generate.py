#列表生成式
a=[x*x for x in range(10)]
b=[x+y for x in "ab" for y in "cd"]
print(a)
print(b)
c=[x*x for x in range(10) if x%2==0]
print(c)

di={"aa":12,"bb":20}
for x,y in di.items():#同时迭代key和value
    print("x y= ",x,y)
e=[x if x%2==0 else -x for x in range(10)]
print(e)

#generator 生成器 也就是储存算法，每次迭代只在内存里面保存一项
gene=(x*x for x in range(10))#使用小括号而不是[]
print(next(gene))#使用next(生成器)获取下一个值

#可以用for来迭代generator
#如果使用了next那么就从next后面接着来
for x in gene:
    print(x)

#def 生成器函数

def gene1(num):
    n,a,b=0,0,1#整体赋值
    while n<num:
        yield b#相当于生成器，就是函数执行到这里就先中断，下次再继续在这里执行
        n,a,b=n+1,b,a+b
    return "done"
f=gene1(10)
#可以采用next(来调用)
#next(f)
for x in f:
    print(x)

#

def yanghui(num):
    a=[1]
    n=0
    while n<num:
        yield a
        a=[1]+[a[n]+a[n+1] for n in range(len(a)-1)]+[1]#拼接，[]其实就是一个数组，可以用下标来迭代的
        #里面如果有不存在的数字那么就不会生成这一项了，这个是利用n+1来控制大小的
        n+=1
f=yanghui(10)
for x in f:
    print(x)
