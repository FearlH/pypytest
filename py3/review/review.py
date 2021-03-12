#1
message="\"你好\""
print(message)

#2
name="\"WQQ\""
love="love"
say_love=f"I {love} {name}"
print(say_love)

#3
name_WQQ="wang qing qing"
print(name_WQQ.lower())
print(name_WQQ.upper())
print(name_WQQ.title())

print("WQQ says I LOVE YOU")
name="WQQ"
says="I LOVE YOU"
print(f"{name} says {says}")
name="\n\tWQQ\t\n"
print(name)
print(name.strip())
print(name.rstrip())
print(name.lstrip())


#4

print(4**4)
print(4+4)
print(9/4)
print(9//4)
print(9%4)

#5

transpotation=["bicycle","train","bus"]
for x in transpotation:
    print(x)

print(transpotation[0])
print(transpotation[-1])
print(f"My favorite transpotation is {transpotation[0]}")

names=["WQQ1","WQQ2"]
for name in names:
    print(f"{name} DO SOMETHING")

#6

transpotation=["bicycle","train","bus"]
transpotation.append("app")
print(transpotation)

del transpotation[3]#位置
transpotation.pop(1)
transpotation.remove("bicycle")

tr=sorted(transpotation,reverse=True)
print(tr)

transpotation.sort()
print(transpotation)

print(transpotation.reverse())#永久的



#7

maps={"key1":"value1","key2":"value2","key3":"value1"}#key重复就保留一个
maps["key4"]="value4"
print(maps)
del maps["key4"]
print(maps)


maps.keys()
maps.values()
maps.items()

maps.get("key1","None")

alien=["aa","bb",["cc","dd"]]
a2=alien[:]
a2[0]="ff"
a2[2][0]="ee"
print(alien)
print(a2)
print("aa" in alien)
#8

def print_person(age,name="aaa",job="bbb",*others,**q):
    print(age,name,job)
    if others:
        print(others)
    if q:
        print(q)

print_person()
print_person(12,"ccc","ddd")
print_person(*[12,"ccc","ddd"])
print_person(*[12,"ccc","ddd"],*["rrr","eee"])
print_person(*[12,"ccc","ddd"],*["rrr","eee"],city="beijing",**{"habit":"do"})
