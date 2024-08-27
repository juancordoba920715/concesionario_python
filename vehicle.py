
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.avalible = True
        
    
       
        
    def vehicle_disponible(self):
        make = input("Ingrese la marca")
        model = input("ingrese el modelo")
        Year = input("ingrese el año")
        self.vehicle_inventory.append(Vehicle(make, model, Year))
        
    def sale_vehicle(self):
        for item in self.vehicle_inventory:
            if self.avalible:
                print(f"El vehiculo {item.make} {item.model} {item.year} es tuyo")
            else:
                print(f"El vehiculo {item.make} {item.model} {item.year} no esta disponible")
                
    def show_vehicle(self):
        self.vehicle_inventory

    