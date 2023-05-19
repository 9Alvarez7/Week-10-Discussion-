
class Vehicle:
    def __init__(self, vehicle_options:dict) -> None:
        self.make = ""
        self.model = ""
        self.vehicle_options = vehicle_options
    
    def setMake(self, make):
        self.make = make
    
    def setModel(self, model):
        self.model = model
    
    def displayOptions(self):
        pass 
    
class Car(Vehicle):
    
    def __init__(self, vehicle_options: dict) -> None:
        super().__init__(vehicle_options)
        self.doors = 0
      
    def setDoors(self, doors):
        self.doors = doors
    
    def displayOptions(self):
        print("Displaying options for Car Vehicle")
        print("Make\tModel")
        print("{}\t{}\n".format(self.make, self.model))
        print("\nVehicle options:")
        for key in self.vehicle_options:
            print("{}\t{}".format(key, self.vehicle_options[key]))
    
class pickuptrucks (Vehicle):
    
    def __init__(self, vehicle_options: dict) -> None:
        super().__init__(vehicle_options)
        self.bedLength = 0.0
    
    def setBedLength(self, bedLength):
        self.bedLength = bedLength
    
    def displayOptions(self):
        print("Displaying options for Trucks Vehicle")
        print("Make\tModel")
        print("{}\t{}\n".format(self.make, self.model))
        print("\nVehicle options:")
        for key in self.vehicle_options:
            print("{}\t{}".format(key, self.vehicle_options[key]))

def menu():
    print("1. To add Car to your virtual garage\n2. To add pickuptruck to your virtual garage\n3. Exit\n")
    choice = int(input("Please enter your choice: "))
    return choice 

def main():    
    cars = []
    pickuptruck = []
    options = []
  
    while True:
        d = {}
        choice = menu()
        if choice == 1:
            make = input("Enter make of your car: ")
            model = input("Enter model of your car: ")
            doors = int(input("Enter the number of doors of vehicle: "))
            options = input("Enter your vehicle options: ")
            options = options.split(",")
            d[make + " " + model] = options
            car = Car(d)
            car.setMake(make)
            car.setModel(model)
            car.setDoors(doors)
            cars.append(car)
            print("Car vehicle has been added in your virtual garage.\n")
        elif choice == 2:
            make = input("Enter make of your pickuptruck: ")
            model = input("Enter model of your pickuptruck: ")
            length = float(input("Enter the length of bed of your vehicle: "))
            options = input("Enter your vehicle options: ")            
            options = options.split(",")
            d[make + " " + model] = options
            pickuptruck = pickuptruck(d)
            pickuptruck.setMake(make)
            pickuptruck.setModel(model)
            pickuptruck.setBedLength(length)
            pickuptruck.append(pickuptruck)            
            print("Pickup vehicle has been added in your virtual garage!\n")
            
        elif choice == 3:
            if len(cars) == 0 or len(pickuptruck) == 0:
                print("Please choose at least one Car and one pickuptruck   vehicle, Thank you.")
                continue
            else:
                for car in cars:
                    car.displayOptions()
                print()
                for pickuptruck in pickuptruck:
                    pickuptruck.displayOptions()
                
        else:
            print("Please choose a valid choice from options [1-3]!")

if __name__ == "__main__":
    main()