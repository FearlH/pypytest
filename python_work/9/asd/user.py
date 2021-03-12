class User:
    def __init__(self,first_name,last_name):
        super().__init__()
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
    def increase_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    def show_login_attempts(self):
        print(self.login_attempts)