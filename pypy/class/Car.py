class Car:
    def __init__(self,make,model,year,odometer=0):
        super().__init__()
        self.make=make
        self.model=model
        self.year=year
        self.odometer=odometer
    def show_car(self):
        print(f"This is a car {self.make}  {self.model}  {self.year}  {self.odometer}")
    def read_odometer(self):
        print(f"odometter is {self.odometer}")
    def update_odometer(self,new_meter):
        if new_meter>self.odometer:
            self.odometer=new_meter
        else:
            print("ERROR")

my_car=Car("audi","newbee",2019)
my_car.read_odometer()
my_car.show_car()
my_car.odometer=10
my_car.read_odometer()
my_car.update_odometer(15)

class Electric_Car(Car):
    def __init__(self, make, model, year, odometer=0):
        super().__init__(make, model, year, odometer=odometer)
my_tesla=Electric_Car("tesla","3379",2019,0)
my_tesla.show_car()

