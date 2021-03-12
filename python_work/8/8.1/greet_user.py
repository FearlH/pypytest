def greet_user(username):
    print(f"Hello {username.title()}!")
greet_user("hhh ll")

def display():
    print("study some function")
display()

def favorite_book(book_name,book_type="book"):
    print(f"The book is {book_name.title()} Type is {book_type}")
favorite_book("Alice","Book")
favorite_book(book_type="book",book_name="Alice")   

# 默认值
def mylove(who,person="wang qing qing"):
    print(f"{who} love {person.title()}")
mylove(who="I")

def make_shirt(size,sentence="I Love Wqq!"):
    print(f"T-shirt size {size},{sentence}")
make_shirt(10)
make_shirt(sentence="I love Wqq",size=20)

def get_full_name(first_name,last_name,middle_name=""):
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}".title()
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()
print(get_full_name("wang","qing","qing"))

def build_person(first_name,last_name,age=""):
    return {"first":first_name.title(),"last":last_name.title(),"age":age}
person=build_person("wang","qing qing",23)
print(person)

while True:
    print("\nPlease tell me your name:")
    print("\nenter q at anytime to quit\n")
    first_name=input("firstname ")
    if first_name=="q":
        print("thanks")
        break
    last_name=input("lastname ")
    if last_name=="q":
        print("thanks")
        break
    person=build_person(first_name,last_name)
    print(person)

def city(city_name,country):
    print(f'"{city_name},{country}"')
city("beijing","china")

def make_album(singer_name,song_name,number=None):
    if not number:
        song_song={"s_name":singer_name,"song":song_name}
    else:
        song_song={"s_name":singer_name,"song":song_name,"number":number} 
    return song_song
print(make_album("wang qing qing","I love you",3))


def greet_perple(names):
    for name in names:
        print(f"\nHello {name}!")
greet_perple(["aaa","bbb","ccc"])
def send_messages(message,to_messages):
    to_messages.append(message)
    return to_messages
def show_messages(messages):
    to_=[]
    for message in messages:
        print(message)
        send_messages(message,to_)
    return to_
messages=["I","Love","Wang Qing Qing"]
to_messages=show_messages(messages)
print(to_messages)


def make_pizza(size,*toppings):
    print(f"size {size}")
    for topping in toppings:
        print(topping)

make_pizza(20,"asdasd","adasd","hdieihuef")

user={}
user["name"]="hhh"
print(user)


    
def make_car(size,**others):
    others["size"]=size
    return others
car=make_car(100,color="red",outback="asdljasdlk")
print(car)




