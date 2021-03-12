import math#定义函数
def quadratic (a,b,c):
    if isinstance(a,(int,float))and isinstance(b,(int,float))and isinstance(c,(int,float)):
        d=b*b-4*a*c
        if d<0:
            raise TypeError("d<0")#异常
        else:
            d=math.sqrt(d)
            return (-b+d)/2/a,(-b-d)/2/a#返回多个值
    else:
        raise TypeError("not number")    

print(quadratic(1,4,3))


#默认参数
def power(x,n=2):#默认n为2，不输入n 那么就按照2来处理
    return x**n#这个就是多少次方

print(power(3))

#如果默认参数不按照顺序写进去，那么就要指定名字

def power2(x,a=1,b=2,c=3):
    pass
#写的时候可以是
# power2(3,b=4) 
#默认参数一般指向不可变对象，指向了可变对象之后，那么随着可变对象被改变值，默认参数的值也会改变

#可变参数

def power3(a,b,*num):#相当于传入一个名字叫做num的list或者tuple
    pass
#调用的时候可以直接写一系列的数字上面的 power3("a","b","c",1,2,3)
#也可以指示一个list或者tuple为可变参数传进去 power3("a","b","c",*[1,2,3])

#传入dict
def power4(a,b,**maps):
    print(maps)

#调用时传入power4(1,2,city="beijing",age=20)
power4(1,2,city="beijing",age=20,)#key不带引号

#传入dict 命名关键字参数
def power5(a,b,*,city,age):#传入dict但是只接受2个key city和age
    print(a,b,city,age)

power5(1,2,city="beijing",age=20)#输出的是对应value值


def power6(a,b,*,city="beijing",age):#也可以设置默认
    pass
