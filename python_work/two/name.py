L=["hello","hhh","bbb","eee","qqq"]
print(L[0])
print(L[-1])
L.append("asd")#添加到最后
L[0]="ccc"
print(L[0])
print(L[-1])
L.insert(1,"rrr")#在指定索引之前插入元素
del L[1]#删除一个索引的元素
name=L.pop()#弹出最后一个
name2=L.pop(1)#弹出索引为1的元素
L.remove("bbb")#删除 "bbb"但是如果有多个 "bbb" 那么删除第一个

persons=["asd","qwe","zxc"]
print(persons[1])
persons[2]="gxt"
print(persons[2])
persons.insert(0,"lh")
persons.insert(2,"lyf")
persons.append("dlrb")

name=persons.pop(1)
print(f"sorry {name} you are poped")

del persons[0]
del persons[1]
print(persons)
persons.remove("gxt")#根据名字删除
print(persons)