class Privileges:
    def __init__(self,priledegs=["aa","cc","dd"]):
        super().__init__()
        self.priviliges=priledegs
    def show_privileges(self):
        for privilege in self.priviliges:
            print(privilege,end=" ")
        print("")