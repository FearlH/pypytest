class Employee:
    def __init__(self,firstname,lastname,salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
    def give_raise(self,money=5000):
        self.salary+=money
