#返回函数，返回的函数会保留外部函数的需要的局部变量的指针，但是不会立即执行
#保留的是指针，所以在调用的时候，会引用指针里面的值，如果指针的值改变了，那么执行的时候
#就会用到改变了的值
def func(x):
    def infun(n):
        return x*x*n#这个里面的X实际上是指向上面X的指针
    x=20#在这里改变了x之后指针就变化了值
    return infun

c=func(10)#c就相当于把x=10带入之后的infun
print(c(2))#当被执行的时候那么就会把常量传入，绑定

def createrCounter():
    c=[0]#使用一个外部变量，每一次调用getc的时候使得外部值增加，返回外部值
    def getc():
        c[0]+=1
        return c[0]
    return getc
getnum=createrCounter()
print([getnum(),getnum(),getnum(),getnum(),getnum(),getnum()])
