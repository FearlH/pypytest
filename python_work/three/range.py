C=range(1,10,2)#[1,10)步长为2

digits=[1,2,3,4,5,6,7,8,9]
min(digits)
max(digits)
sum(digits)
print(digits[1:4])#[1,4)索引
#对于字符串操作都是返回一个新字符串
car="Audi"
lower_car=car.lower()#不会影响原来的值
print(lower_car,car)

print(10 in digits)
print(10 not in digits)

if digits:#列表为空返回0不为空返回1
    print(1)
else:
    print(0)
print([1,2,3,4,
5,6,7,8,9])

alien={"color":"blue","age":10}
for key,value in alien.items():#返回键值对列表
    print(key,value)

alien.keys()
alien.values()
alien["name"]="dodone"#这样在里面添加
for x ,y in alien.items():
    print(x,y)


def func(name,age=15,*other):
    print("name=",name," age=",age)
    for x in other:
        print(x)

func("aaa","bbb","ccc")#还是把前面的填满然后后面的值组成一个列表
func("aaa",*[1,"bbb","ccc"])#相当于把这个list拆开变成一系列的元素

from python_work.three.pizza import *
printa()
make_pizza()


