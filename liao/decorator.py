#装饰器，给一个函数，返回一个函数
import functools
def write_name(func):
    @functools.wraps(func)##123
    def write(*args,**more):
        print("哈哈")
        print(func.__name__)
        return func(*args,**more)
    return write#这里面返回的函数名称变成了write
    #要使得返回函数的名称和func参数名称一样那么就要加上一个 ##123对应的内容
    #return write   write按照参数执行的时候就会先执行 其他内容，然后执行func
    # 然后返回执行的结果

#加上了这个之后相当于 wr=write_name(wr)
#因为里面赋值了名字，所以wr的名字不是write而还是wr

#@write_name 语法不对
def wr(a):
    print(a+1)
    return "执行完毕"
print(wr(3))


#偏函数
import functools
def plus(x,n):
    return x+n
plus2=functools.partial(plus,n=2)#把plus的参数固定几个，生成一个新的函数
print(plus2(1))