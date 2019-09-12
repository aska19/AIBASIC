
# class Robot:
#     def __init__(self,name):
#         self.name = name
#     def introduce_yourself(self):
#         print("My name is " + self.name)

# robot1 = Robot("Tom")
# robot1.introduce_yourself()
# print(robot1.name)

# robot2 = Robot("Jan")
# robot2.introduce_yourself()



# class Robot:
#     def __init__(self,name="Lorem"):
#         self.name = name
#         self.color = "Red"
#     def introduce_yourself(self):
#         print("My name is " + self.name)

# robot1 = Robot("Tom")
# robot1.introduce_yourself()
# print(robot1.name)

# robot2 = Robot("Jan")
# robot2.introduce_yourself()

# robot3 = Robot()
# robot3.introduce_yourself()



# class Robot:
#     def __init__(self,name):
#         self.name = name
#         self.color = "Red"
#         self.energy = 100
    
#     def introduce_yourself(self):
#         print("My name is " + self.name)
    
#     def jump(self):
#         self.energy -= 10
#         return self.energy

# robot1 = Robot("Tom")
# robot1.introduce_yourself()
# robot1.jump()
# robot1.jump()
# robot1.jump()
# print("Your Energy left are",robot1.energy)



# class Robot:
#     def __init__(self,name):
#         self.name = name
#         self.color = "Red"
#         self.energy = 100
    
#     def introduce_yourself(self):
#         print("My name is " + self.name)
    
#     def jump(self):
#         if self.energy <= 50 and self.energy != 0:
#             print("low energy")
#             self.energy -= 10
#         elif self.energy >= 50:
#             self.energy -= 10
#         elif self.energy == 0:
#             print("Empty Energy")
#         return self.energy

# robot1 = Robot("Tom")
# robot1.introduce_yourself()
# robot1.jump()
# robot1.jump()
# robot1.jump()
# robot1.jump()
# robot1.jump()
# robot1.jump()
# print("Your Energy left are ",robot1.energy)



####

# 
# class Car:
#     def __init__(self,name,color,unitcode):
#         self.name = name
#         self.color = color
#         self.unitcode = unitcode
#         self.speed = 0
#         self.speedlimit = 160
#         self.fuel = 0
#         self.fuellimit = 40
    
#     def introduce_car(self):
#         print("Brand : " + self.name + "color : " + self.color + "unitcode : " + self.unitcode)

#     def speedup(self):
#         if self.speed >= 0 and self.speed <= self.speedlimit:
#             print("You are in speedlimit")
#             self.speed += 10
    
#     def speeddown(self):
#         if self.speed >= 10 and self.speed == 0:
#             print("You are in fuellimit")
#             self.speed -= 10

#     def gasup(self):
#         if self.fuel >= 0 and self.fuel == self.fuellimit:
#             print("You are in fuellimit")
#             self.fuel += 5

#     def gasdown(self):
#         if self.fuel < 40 and self.fuel == 0:
#             print("Empty Gas")
#             self.fuel -= 5

# print("Create Your Car now!!")
    
# Brand = str(input("Enter the brand name : "))
# Color = str(input("Enter the Color : "))
# Unitcode = str(input("Enter the unitcode : "))

# car1 = Car(Brand,Color,Unitcode)
# while True:

#     print("Try Your Car now")
#     print("[1] speedup")
#     print("[2] speeddown")
#     print("[3] gasup")
#     print("[4] gasdown")
#     print("[5] stop")

#     number = int(input("choice : "))

#     if number == 1:
#         car1.speedup()
#     if number == 2:
#         car1.speeddown()
#     if number == 3:
#         car1.gasup()
#     if number == 4:
#         car1.gasdown()
#     else:
#         break



###

class Car:
    def __init__(self,name,color,unitcode):
        self.name = name
        self.color = color
        self.unitcode = unitcode
        self.speed = 0
        self.speedlimit = 160
        self.fuel = 0
        self.fuellimit = 40
    
    def introduce_car(self):
        print("Brand : " + self.name + "color : " + self.color + "unitcode : " + self.unitcode)

    def speedup(self):
        if self.fuel > 0:
            self.speed += 10
            self.speed -= 2
        if self.speed >= 0 and self.speed <= self.speedlimit:
            print("You are in speedlimit")
        
    
    def speeddown(self):
        if self.speed >= 10 and self.speed == 0:
            print("You are in fuellimit")
            self.speed -= 10

    def gasup(self):
        if self.fuel >= 0 and self.fuel == self.fuellimit:
            print("You are in fuellimit")
            self.fuel += 5

    def gasdown(self):
        if self.fuel < 40 and self.fuel == 0:
            print("Empty Gas")
            self.fuel -= 5

print("Create Your Car now!!")

car_list = [ ]
num = int(input("How many car do you want to create? : "))

for i in range(0,num):
    car_dict = {}
    car_dict["Brand"] = input("What is brand? :")
    car_dict["Color"] = input("What is color? :")
    car_dict["unitcode"] = input("What is unitcode? :")

    print(car_list.append(car_dict))

# Brand = str(input("Enter the brand name : "))
# Color = str(input("Enter the Color : "))
# Unitcode = str(input("Enter the unitcode : "))

car1 = Car(car_dict["Brand"],car_dict["Color"],car_dict["unitcode"])

while True:

    print("Try Your Car now")
    print("[1] speedup")
    print("[2] speeddown")
    print("[3] gasup")
    print("[4] gasdown")
    print("[5] stop")

    number = int(input("choice : "))

    if number == 1:
        car1.speedup()
        continue
    elif number == 2:
        car1.speeddown()
        continue
    elif number == 3:
        car1.gasup()
        continue
    elif number == 4:
        car1.gasdown()
        continue
    elif number == 5:
        break