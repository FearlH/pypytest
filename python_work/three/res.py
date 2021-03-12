from python_work.three.dog import Restaurant as RE
class New_York_Rest(RE):
    def __init__(self,name,type,size):
        super().__init__(name,type)#不要忘记super()
        self.size=size
    def show_restaurant(self):
        self.describe_restaurant()
    def open_restaurant(self):#重写
        print("OPEN!")
        return super().open_restaurant()
a_re=New_York_Rest("oho","dinner",20)
a_re.show_restaurant()
print()
a_re.show_restaurant()
    