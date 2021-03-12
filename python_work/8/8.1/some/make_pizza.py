def pizza(
        size,
        **others):
    others["size"]=size
    print(others)
    for x,y in others.items():
        print(x,y)
    return others
def love():
    print("I Love Wqq")