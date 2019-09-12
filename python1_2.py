# x = 10%2

# print(x)


# y = [1,2,3,4,5]
# z = [6,7,8,9,10]
# w = 2 in y
# r = 2 not in y

# print(w)
# print(r)

# name = "jan"
# age = 25;

# print("my name is {}".format(name))
# print("my name is {} and i am {} year yong".format(name,age))


"""
This is a coment
"""


# name = "Jan-Joven Jumao-as"
# print(name[0])
# print(name.split(" "))
# print(name.split("-"))

# splitedname = name.split("-")
# print("@".join(splitedname))

# splitedname = " ".join(name.split("-"))
# print(splitedname)

# name = "        janjove       "
# print(name)
# print(name.strip())

"""
# age = int(input("How old are you ?"))

# if age > 20 and age < 60:
#     print("You are in legal age!")
# elif age > 60 and age < 120:
#     print("You are already great person")
# else:
#     print("You are under age")
"""

"""
# for i in range(1,11):
#     print(i)


# students = ["hiro","chika","asuka"]

# for student in students:
#     print(student)


students = [{"name":"hiro"},{"name":"chika"},{"name":"asuka"}]

for student in students:
    print(student["name"])
"""


# x = 0

# while x < 10:
#     print(x)
#     x += 1


# while True:
#     question = input("Do you want to quit? Y/N : ")

#     if question == "Y":
#         break
#     else:
#         continue


###

# while True:
#     question = input("Enter a number:")

#     if question == "100":
#         break
#     else:
#         continue


# ###
# number = int(input("Enter a number:"))
# for i in range(0,number):
#     if i%2 == 0:
#         print(i)


number = input("Enter a number : ")

splited_number = " ".join(number)
splited_number = splited_number.split(" ")
print(splited_number)

roman_numeral = [{"1":"I","4":"IV","5":"V","9":"IX","10":"X","50":"L","100":"C","500":"D","1000":"M"}]

i = 0

for number in range(len(splited_number)):
    if splited_number[i] == roman_numeral[j]: