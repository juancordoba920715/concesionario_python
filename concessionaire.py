

class Concessionarie:
    
    def __init__(self):
        
        self.vehicles = []
        self.users = []
        
    def sale(self):
        if self.avalible:
            self.avalible = False
            return f"Vehicle {self.make} {self.model} {self.year} is sold"
        else:
            return f"Vehicle {self.make} {self.model} {self.year} is not aval"
        
    def shop(self):
        self.avalible
        