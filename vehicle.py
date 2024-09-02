from concessionaire import vehicles
class Vehicle:
    def __init__(self,id_vehicle,  make, model, year):
        self.id_vehicle = id_vehicle
        self.make = make
        self.model = model
        self.year = year
        self.available = True
        
        
    def add_vehicle(self, vehicle:Vehicle):
        if vehicle in vehicles:
            print(" is olready exist")
        else:
            vehicles.append(vehicle)
            print("added Vehicle")
            
    def delete_vehicle(self, vehicle: Vehicle):
        if vehicle in vehicles:
            vehicles.remove(vehicle)
            print("Vehicle deleted")
        else:
            print("Vehicle not found")
            
    def update_vehicle(self, vehicle: Vehicle):
        if vehicle in vehicles:
            for item in vehicles: 
                ite      
    
       
        
    def is_available(self):
        if self.available:
            return f"{self.year} {self.make} {self.model} is available"
        else:
            return f"{self.year} {self.make} {self.model} is not available"
            
        
    
            
            
        
        
    