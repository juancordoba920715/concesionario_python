from concessionaire import users

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vehicles_purchased = []
        
    def add_user(self, user):
        users.append(user)
        print(f("Usuario agregado"))
        