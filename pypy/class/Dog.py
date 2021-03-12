class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def roll(self):
        print("roll")
    def sit(self):
        print("sit")




my_dog=Dog("abc",3)

print(f"my dog's name is {my_dog.name}","and",f"its age is {my_dog.age}")
a="abc"+"bcd"
print(a)
my_dog.roll()
my_dog.sit()

your_dog=Dog("bbb",4)


class Resaurant:
    def __init__(self,name,_type):
        self.name=name
        self.type=_type
    def describe_resaurant(self):
        print(f"This resaurant is in {self.type} type. Name is {self.name}")
    def open(self):
        print("open")

class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        super().__init__()
    def greet_user(self,to_someone):
        print(f"Hello {to_someone}")
    

my_res=Resaurant("aaa","BeiJingDuck")
my_res.describe_resaurant()
my_res.open()

user_one=User("aaa","bbb")
user_one.greet_user("ccc")

