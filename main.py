from concessionaire import users, vehicles
from user import User
from vehicle import Vehicle

opcion = 0

print("Welcome to Car dreams")

print("Opciones:\n 1: Users\n 2: Vehicles\n 3: Concessionarie\n 4: SALIR ")

while opcion:

    match opcion:
        case 1 :
            print("1:Registrar usuario\n 2: actualicar usurio\n 3: Borrar usuario")
            match opcion:
                case 1:
                    User.add_user()
                    break
                case 2:
                    User.update_user()
                    break
                case 3:
                    User.delete_user()
                    break
        case 2 :
            print("1: Registrar vehiculo\n 2: Actualizar vehiculo\n3: Borrar vehiculo ")
            match opcion:
                case 1:
                    Vehicle.add_vehicle()
                    break
                case 2:
                    Vehicle.update_vehicle()
                    break
                case 3:
                    Vehicle.delete_vehicle()
                    break



User.add_user()
User.add_user()
Vehicle.add_vehicle()
Concessionarie.sale()
User.vehicles_purchased()