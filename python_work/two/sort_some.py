L=[2,4,1,3,1,7,8,5,6,9,1,2,3,4,5,6,8,7,1]
L.sort()#永久排序
print(L)
L.sort(reverse=True)
print(L)
P=sorted(L)#L并不变
P.reverse()#倒着来
num=len(P)#长度

place=["beijing","new york","lendon","amsterdam"]
print(place)
sort_place=sorted(place)#这样的都不改变原始值
print(sort_place)
print(place)
print(sorted(place,reverse=True))
place.reverse()#对于place进行reverse操作
print(place)
place.sort()
print(place)
place.reverse()
print(place)


L=["ad","ap","tank","jugle"]
print(sorted(L))
L.sort(reverse=True)
print(L)


