#1
name = "Mike"
age = 25

intro = "my name is " + str(name) + " and my age is " + str(age) + " years old." 

print(intro)


#2
weight = input("Input your weight(kg)")
height = input("Input your height(m)")

bmi = int(weight) / (int(height)^2)

print(bmi)


##3
student = ["ichiro","jiro","saburo","siro","goro"]

print(student[0])
print(student[1:4])


##4
student_dictionary = {"ichiro":"170","jiro":"180","saburo":"165","siro":"175","goro":"185"}
print(student_dictionary["siro"])


##5
student_list = [{"name":"ichiro","english":"55","japanese":"60","math":"70"},
                {"name":"shiro","english":"70","japanese":"80","math":"90"},
                {"name":"goro","english":"90","japanese":"60","math":"80"}]
print(student_list[1]["english"])


##6
x = input("Enter any number here x=")
y = input("Enter any number here y=")

print("x + y = " , int(x) + int(y))


##7
x = input("Enter any number here x=")

if x >= 50:
    print("up")
else:
    print("down")


##8
fruits = ["apple" , "orange" , "grape"]

for n in fruits:
    print(n)


##9
x = 10
while x > 0:
    print(str(x))
    x -= 1