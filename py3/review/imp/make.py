
def print_person(age,name="aaa",job="bbb",*others,**q):
    print(age,name,job)
    if others:
        print(others)
    if q:
        print(q)