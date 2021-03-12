print('''
line1
line2
''')#在这个里面自己换行

a=len("你好")#字符数
print(a)
a=len("你好".encode("utf-8"))#字节数
print(a)
c="你好%s,你几岁.%d岁"%("哈哈",12)
print(c)

#list 和 tuple
list1=[1,2,3,4,5,"aaa",[1,4,7],True]#里面什么都可以填进去
print(list1)
list1.append("eee")
print(list1)

something=list1.pop(2)#不写默认是最后一个
print(list1)
print(something)

list1[2]="2替换"#不会返回替换的原始值
print(list1)

#tuple不可改变的list
tuple1=(1,2,3)
tuple2=(1,["aa","bb","cc"],True)#这样里面的list可以改变
print(tuple1)
print(tuple2)
tuple2[1].append("dd")#索引从0开始
print(tuple2)
(1,)#一个元素的tuple 防止与(1)一个小括号1相同

#tuple() list[]都是有序可以带索引的

#python用一个tab或者4个空格缩进

a=10
if a>0:#需要加一个：表示一个语句的开始，后面不缩进表示结束
    print("a>0")
else:
    print("a<0")

# input()输入
some3=input("请输入")#里面填提示符 返回str

some3=int(some3)#转换为int(some3)不是(int)some3
print(some3*2)
if some3<0:
    print("小于0")
elif some3==0:
    print("等于0")
else:
    print("大于0")
#以上的if在运行文件的时候就是对的，运行选中运行就不对了
'''
行运行就是一行一行地运行比如
some3=input("请输入")#里面填提示符 返回str
#注释
some3=int(some3)#转换为int(some3)不是(int)some3
在some3=input("请输入")一步一步输入
之后本来命令行应该直接获取到你想要的东西
就是直接输入一个东西，但是因为后面一行又有了一些东西，就会出现错误

some3=input("请输入")
请输入123
会把123放入some3里面

但是
下面这些直接黏贴到命令行里面

some3=input("请输入")
#注释

相当于输入了#注释

但是运行整体文件不会这样
#里面的被当做注释看待
而不是输入

键入代码就是一行一行的，就是按照行执行的样子


'''














