'''
切片
'''
L=list(range(10))#0-9
print(L)

#L[a:b:c] 从[a,b)每隔c取一个数 索引从0开始

F=L[1:7:2]
print(F)
F=L[-4:]#啥也不写表示开始或者最后 还可以倒着取-4代表倒数第4个

# list tuple str 都可以切 

#去掉字符串空格
'''
def trim(L):
    while True:
        if len(L)==0:
            return L
        elif L[:1][0]==' ':
            L=L[1:]
        elif L[-1:][0]==' ':
            L=L[:-1]
        else:
            break
    return L

'''
def trim(L):
    i=0
    j=-1
    for x in list(range(len(L))):
        if L[i]==' ':
            i+=1
        else:
            break
    for x in list(range(len(L))):
        if L[j]==' ':
            j-=1
        else:
            break
    return L[i:len(L)+j+1]
print(trim(" adada "))


