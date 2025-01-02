# Question 1:

# class Car:
#     def __init__(self,brand,model="latest"):
#         self.brand=brand    
#         self.model=model    
        
# myCar=Car("Toyota","Corolla")
# print(myCar.brand)
# print(myCar.model)

# myCar2=Car("Honda","Civic")
# print(myCar2.brand)
# print(myCar2.model)


# Question 2:

# class Car:
#     def __init__(self,brand,model="latest"):
#         self.brand=brand    
#         self.model=model   
    
#     def fullName(self):
#         return f"{self.brand}  {self.model}" 
        
# myCar=Car("Toyota","Corolla")
# print(myCar.fullName())


# Question 3:


# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand    
#         self.model=model   
    
#     def fullName(self):
#         return f"{self.brand}  {self.model}" 

# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size
        
# myCar=ElectricCar("Tesla","Model S","85KWH")
# print(myCar.model)
# print(myCar.fullName())


#Question 4:

# class Car:
#     def __init__(self,brand,model):
#         self.__brand=brand    
#         self.model=model
#     def get_brand(self):
#         return self.__brand

# myCar=Car("Tesla","Model S")
# # print(myCar.__brand)
# print(myCar.get_brand())


#Ouestion 5

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def fuel_type(self):
#         return "Petrol and Diesel"
        
#     def full_name(self):
#         return f"{self.brand} {self.model}" 

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electricity"

# # Create instances of Car and ElectricCar
# myCar1 = Car("Toyota", "Corolla")
# print(f"{myCar1.full_name()} uses {myCar1.fuel_type()} as fuel.")

# myCar2 = ElectricCar("Tesla", "Model S", 100)
# print(f"{myCar2.full_name()} uses {myCar2.fuel_type()} as fuel.")


#Question 6:

# class Car:
#     total_car=0
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_car+=1

#     def fuel_type(self):
#         return "Petrol and Diesel"
        
#     def full_name(self):
#         return f"{self.brand} {self.model}" 

# myCar1 = Car("Toyota", "Corolla")
# myCar2 = Car("Honda", "Civic")
# myCar3 = Car("Tesla", "Model S")

# print(f"Total number of cars created: {Car.total_car}")


#Question 7:

# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand    
#         self.model=model
    
#     @staticmethod   #decorators
#     def generalDiscription():
#                 return "A car is a vehicle with four wheels, used for transportation."
        
# myCar=Car("Toyota","Corolla")
# print(Car.general_description("Toyota", "Corolla"))


#Question 8:


# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand    
#         self.__model=model
        
#     @property
#     def model(self):
#         return self.__model
    
# myCar=Car("Toyota","Corolla")
# # myCar.model="Civic"
# print(myCar.model)



#Question 9:


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def fuel_type(self):
#         return "Petrol and Diesel"
        
#     def full_name(self):
#         return f"{self.brand} {self.model}" 

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

# my_tesla=ElectricCar("Tesla","Model S","85KWH")
# print(isinstance(my_tesla,ElectricCar))
# print(isinstance(my_tesla,Car))



#Question 10:

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "The car has a 85KWH battery."
class Engine:
    def engine_info(self):
        return "The car has a 3.5L V6 engine."

class ElectricCar(Battery,Engine,Car):
    pass

my_tesla=ElectricCar("Tesla","Model S")
print(my_tesla.battery_info())
print(my_tesla.engine_info())