from privilege import Privileges
from user import User
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilidges=Privileges()
    def show_priviledges(self):
        self.privilidges.show_privileges()
        print("")
a_admin=Admin("aaa","bbb")
a_admin.show_priviledges()
a_admin.greet_user()