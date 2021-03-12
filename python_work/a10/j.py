import json
numbers=[0,1,2,3,4,5,6,7,8,9]
filename="python_work\\a10\\joo.json"
with open(filename,"w") as f:
    json.dump(numbers,f)
with open(filename,"r") as f:
    read_num=json.load(f)
print(read_num)


user_root="python_work\\a10\\jio.json"
try:
    with open(user_root) as ur:
        name=json.load(ur)
except FileNotFoundError:
    with open(user_root,"w") as ur:
        name=input("enter your name:")
        json.dump(name,ur)
else:
    print(f"Hello {name}")



def write_user_name(file_name):
    name=input("enter your name:")
    with open(file_name,"w") as f:
        json.dump(name,f)
def get_user(file_name):
    try:
        with open(file_name) as f:
            name=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name
def greet_user():
    user_root="python_work\\a10\\jio.json"
    user_name=get_user(user_root)
    if user_name:
        print(f"Hello {user_name}")
    else:
        write_user_name(user_root)
greet_user()

