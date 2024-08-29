from vehicle import Vehicle
from concessionaire import users

class User:
    def __init__(self,id_user, name, age):
        self.id_user = id_user
        self.name = name
        self.age = age
        self.vehicles_purchased = []
        
    def add_user(self, user):
        if user in users:
            print("User already exists")
        else:
            users.append(self)
            print("User add")
            
    def delete_user(self, user):
        if user in users:
            users.remove(user)
            print("User deleted")
        else:
            print("User does not exist")
            
    def update_user(self, user):
        if user in users:
            for item in users:
                item.id_user == user.id_user
                item.name = user.name
                item.age = user.age
                print("User updated")
        else:
            print("User dont exist")
        
            
    def number_vehicle(self):
        number = len(self.vehicles_purchased)
        return number
        
        
    def return_vehicle(self, vehicle):
        if vehicle in self.vehicles_purchased:
            self.vehicles_purchased.remove(vehicle)
            Vehicle.avalible = True
        else:
            print("Vehiculo no comprado")
            
    
            
            
            
        
        
   
        