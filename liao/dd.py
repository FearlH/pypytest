#迭代 先判断是不是属于 Iterable
from collections.abc import Iterable
L=[1,2,3]
C={"city":"beijing","age":20}
if isinstance(C,(Iterable)):#迭代出来的是key
    for x in C:
        print(x,"=",C.get(x))#,是空格，end="..."是在输出语句最后输出一个什么
for x,y in [(1,2),(3,4)]:
    print(x,y)
