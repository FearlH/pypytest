class Resaurant:
    def __init__(self,resaurant_name,cuisine_type):
        super().__init__()
        self.resaurant_name=resaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_resaurant(self):
        print(f"name is {self.resaurant_name} type is {self.cuisine_type}\
 {self.number_served}")
    def set_number_served(self,number):
        if number>0:
            self.number_served=number
        else:
            print("cannot < 0")
    def increment_number_served(self,increase_number):
        if increase_number>0:
            self.number_served+=increase_number
        else:
            print("cannot < 0")