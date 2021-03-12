class Dog:
    def __init__(self,name,age):
        super().__init__()
        self.n=name#相当于在这个里面定义了类属性
        self.age=age
        #类属性里面有n和age
    def sit(self):
        print(self.n)

    def roll(self):#默认调用函数的时候会把self传递进去，所以函数需要定义的时候传递一个self

        print("roll")

a_dog=Dog("ohha","3")
a_dog.roll()
print(a_dog.n)

class Restaurant:#每一个函数都要定义一个self，因为在调用的时候会传入一个self
    def __init__(self,name,type):#都在init里面定义属性
        self.restaurant_name=name
        self.restaurant_type=type
        self.location="beijing"
    def describe_restaurant(self):
        print(self.restaurant_name)#self.才是本地属性
        print(self.restaurant_type)
        print(self.location)
    def open_restaurant(self):
        print("open")
    def update_location(self,new_location):
        self.location=new_location

restaurant=Restaurant("ahoool","dinner")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.location="new york"#更改值
restaurant.update_location("lendon")
restaurant.describe_restaurant()
class City:
    def __init__(self,city_name):
        self.city_name=city_name
    def show_city(self):
        print(self.city_name)

class BeijingRes(Restaurant):#圆括号里面指定父类名称
    def __init__(self, name, type,size,city_name):##init是要定义的
        super().__init__(name, type)
        self.size=size
        self.city=City(city_name)
    
    def show(self):
        print(self.restaurant_name,self.restaurant_type,self.location,self.size)
beijingRes=BeijingRes("oho","dinner",200,"beijing")
beijingRes.city.show_city()



    



