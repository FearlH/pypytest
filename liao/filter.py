#filter是根据规则来选择数据，map是根据规则一个个应用于数据，reduce是根据规则两两作用于所有数据
#根据规则返回的True还是Flase
def isodd(x):#规则
    if x%2==0:
        return False
    else:
        return True
L=filter(isodd,range(20))#把每一个元素带入到isodd里面
print(list(L))
#一个函数就相当于他的返回值
def is_n_times(n):
    def times(x):
        if x%n==0:
            return True
        else:
            return False
    return times
L=filter(is_n_times(3),range(100))
print(list(L))

#sorted 里面可以传入一个key=一个函数名，表示对于每个单项先进行函数名函数的运算，根据返回值进行排序
#但不会影响原来的值

L=["aaa","bbb","CCC","DDD","fff"]
R=sorted(L,key=str.lower)
print(R)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def name_sort(X):
    return X[0].lower()
R=sorted(L,key=name_sort)
print(R)
def pro_sort(X):
    return X[1]
R=sorted(L,key=pro_sort)
print(R)