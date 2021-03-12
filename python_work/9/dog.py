from asd.privilege import Privileges
from asd.user import User
from asd.resaurant import Resaurant

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilidges=Privileges()
    def show_priviledges(self):
        self.privilidges.show_privileges()
        print("")


class IceCreamStand(Resaurant):
    def __init__(self, resaurant_name, cuisine_type,*flavors):
        super().__init__(resaurant_name, cuisine_type)
        self.flavors=flavors
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand=IceCreamStand("ice","aaa","asd","zxc","qwe")
ice_cream_stand.show_flavors()

a_resaurant=Resaurant("aaa","ccc")
a_resaurant.describe_resaurant()
a_resaurant.number_served=3
a_resaurant.set_number_served(4)
a_resaurant.increment_number_served(3)

class Dog:
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age
    def roll(self):
        print(f"{self.name} is rolling")
    def sit(self):
        print(f"{self.name} is sitting")

my_dog=Dog("hhh",3)
print(my_dog.age)
print(f"my dog's name is {my_dog.name}")

my_dog.roll()
your_dog=Dog("ppp",4)

print(your_dog.age)





