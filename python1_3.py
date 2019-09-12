# y = 1**2 + 3*1 +2
# print(y)

# def f(x):
#     y = x*2 + 3*x + 2
#     print(y)
# number = 3
# f(number)

# def f(x,z):
#     y = x**2 + 3*x + z
#     print(y)
# number = 10
# x = 3
# f(x,number)

# def f(x,z=0):
#     y = x**2 + 3*x + z
#     print(y)
# x=3
# f(x)

# def add(x,y):
#     total = x + y
#     print(total)
# add(2,4)

# def add(x,y):
#     total = x + y
#     return total
# print(add(2,4))
# print(add(2,4)*add(5,3))

# def even_odd():
#     n = int(input("Enter a number :"))
#     if n%2 == 0:
#         print("n is even number")
#     else:
#         print("n is an odd number")
# even_odd()

###exercise
# ##(1) after you gave two number, please create a function to multiply
# def multiply(x,y):
#     answer = x * y
#     print(answer)
# x = int(input("Enter a number :"))
# y = int(input("Enter a number :"))
# multiply(x,y)

# ##(2) Create a function that display "HelloWorld" as many as you give to the argument
# def word(x):
#     for i in range (0,x):
#         print("Hello World")
# number = int(input("Enter a number :"))
# word(number)

# number=[1,2,3,4]
# print(len(number))
# print(sum(number))
# print(max(number))
# print(min(number))

# x=5
# def f():
#     x = 10
#     y = 3
#     return x + y

# def g():
#     return x 

# print(f())
# print(g())


# x=5
# def f():
#     global x
#     x = 10
#     y = 3
#     return x + y

# def g():
#     global x 
#     x = 20
#     return x 

# print(f())
# print(g())


##homework1-4 no.4

# def sale(x,y,z,w):
#     price = 0
#     if 15<= y and y <= 24:
#         price = (w * z) * 0.9
#     elif z >= 5:
#         price = (w * z) * 0.9
#     else:
#         price = w * z
#     print("Total amount of " + str(x) + " is " + str(price))
    
# name = input("What are your name ? :")
# time = int(input("What time is it ? :"))
# number = int(input("How many do you buy ? :"))
# price = int(input ("How much is it ? : "))
# sale(name,time,number,price)


###
##exercise

# def add(x,y):
#     total = x + y
#     return total

# def sub(x,y):
#     total = x - y
#     return total

# def mul(x,y):
#     total = x * y
#     return total

# def divi(x,y):
#     total = x / y
#     return total

# while True:
#     print("[1] addition")
#     print("[2] subtraction")
#     print("[3] multiplication")
#     print("[4] division")

#     x = int(input("Enter a number x=:"))
#     y = int(input("Enter a number y=:"))
#     choice = int(input("Choose an operator to perform :"))
#     total = 0
#     if choice == 1:
#         total = add(x,y)
#     if choice == 2:
#         total = sub(x,y)
#     if choice == 3:
#         total = mul(x,y)
#     if choice == 4:
#         total = divi(x,y)
    
#     print(total)
    
#     question = input("Do you want to continue Y/N? :")
#     if question == "Y":
#         continue
#     else:
#         break



# class MyCar:

#     def __init__(self,brand,color,code):
#         self.brand = brand
#         self.color = color 
#         self.code = code

#         print("Car Brand {} , color {} , code {}".format(self.brand,self.color,self.code))

# MyCar("Toyota","Red","xoo9")

##
# class MyCar:

#     def __init__(self,brand,color,code):
#         self.brand = brand
#         self.color = color 
#         self.code = code
#         self.speed = 0

#         print("Car Brand {} , color {} , code {}".format(self.brand,self.color,self.code))
    
#     def speedup(self):
#         self.speed += 10
#         return self.speed

# Toyota = MyCar("Toyota","Red","x009")

# while True:
#     speed = input("enter to speedup")
#     if speed == "s":
#         print("Your Car speed is",Toyota.speedup())
#         continue
#     else:
#         break

##
# class MyCar:

#     def __init__(self,brand,color,code):
#         self.brand = brand
#         self.color = color 
#         self.code = code
#         self.speed = 0

#         print("Car Brand {} , color {} , code {}".format(self.brand,self.color,self.code))
    
#     def speedup(self):
#         self.speed += 10
#         return self.speed

# Toyota = MyCar("Toyota","Red","x009")
# Isuzu = MyCar("Isuzu","Black","x010")

# while True:
#     speed = input("enter to speedup")
#     if speed == "st":
#         print("Your Car speed is",Toyota.speedup())
#     if speed == "si":
#         print("Your Car speed is",Toyota.speedup())
#         continue

#     else:
#         break


####

class MyCar:

    def __init__(self,brand,color,code):
        self.brand = brand
        self.color = color 
        self.code = code
        self.speed = 0

        print("Car Brand {} , color {} , code {}".format(self.brand,self.color,self.code))
    
    def speedup(self):
        self.speed += 10
        return self.speed
    
    def speeddown(self):
        self.speed -= 10
        return self.speed

Toyota = MyCar("Toyota","Red","x009")
Isuzu = MyCar("Isuzu","Black","x010")

while True:
    speed = input("enter to speedup")
    if speed == "st":
        print("Your Car speed is",Toyota.speedup())
    if speed == "si":
        print("Your Car speed is",Toyota.speedup())
        continue

    else:
        break