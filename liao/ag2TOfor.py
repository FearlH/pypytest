#for
names=["aaa","bbb","ccc"]
for name in names:
    print(name,end=" ")#end=..就是输出一个东西结尾带着什么#默认是换行

print("aaa","bbb")#里面接收多个输入，多个输入之间输出的时候中间插入空格

ran=range(5)#生成0到5的整数
a=list(ran)#把range转化为list
print(a)

#break
for x in list(range(10)):
    print(x)
    if x>3:
        break


#dict 里面采用了hash表 相当于map
#一个key只能放进去一个value
'''
多个value放入一个key里面后面的会把前面的替代掉

key in dict 判断key是否在dict里面


'''
# dict 里面的key必须是不可变的量 python字符串、整数等都是不可变的
d={"aaa":123,"bbb":233}
print(d)
print("aac" in d)#判断是否在里面
getsome=d.get("aac","no")#得到key对于的value值
#如果value不存在那么返回第二个自定义的参数
print(getsome)

#删除一个键值对
some=d.pop("aac")#没有key就抛出异常
print(some)
some=d.pop("aaa")#返回value值
print(some)


#set
setone=set([1,2,3,4,5,6,7,8,9])#创建一个set要提供一个list or tuple为输入
print(setone)
s=set((1,2,3))
print(s)
s.add("a")#添加一个
print(s)

s.remove(1)#删除一个
print(s)

andand=s&setone#交集
oror=s|setone

print(andand)
print(oror)




