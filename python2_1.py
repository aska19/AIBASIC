# class Car:
#       def __init__(self):
#             self.secretkey = "123xx22"
#       def mysecretkey(self):
#             print("SecretKey: " + self.secretkey)

# print(Car().secretkey);
# Car().mysecretkey();


# class Car:
#       def __init__(self):
#             self.__secretkey = "123xx22"
#       def getter(self):
#             return self.__secretkey
#       def setter(self,seckey):
#           self.__secretkey = seckey

# Car().setter("asdasdww")
# car1 = Car()
# car1.setter("12344ssxxx")
# print(car1.getter())


# class Person:
#       def __init__(self,name,age,address):
#             self.name = name
#             self.age = age
#             self.address = address
      
#       def information(self):
#             print("Name : {} \n Age : {} \n Address : {} \n".format(self.name,self.age,self.address))

# class Student(Person):
#       def __init__(self,name,age,address,yearlvl):
#             super().__init__(name,age,address)
#             self.yearlvl = yearlvl
      
#       def studentinfo(self):
#             print("Name : {} \n Age : {} \n Address : {} \n Yearlvl : {}\n".format(self.name,self.age,self.address,self.yearlvl))

# class Teacher(Person):
#       pass

# student = Student("Jan",25,"Cebu",3)
# student.studentinfo()


# import os
# import subprocess as np

# info_list = []
# class Person:
#       def __init__(self,name,age,address):
#             self.name = name
#             self.age = age
#             self.address = address
#             self.info_list = []
#       def information(self):
#             print("Name : {} \n Age : {} \n Address : {} \n".format(self.name,self.age,self.address))
#       def saveinformation(self,wtype):
#             information_dict = {"name":self.name , "age":self.age , "address":self.address , "type":wtype}
#             info_list.append(information_dict)
#       #def getinformation(information):
#       #      return self.info_list

# class Student(Person):
#       def __init__(self,name,age,address,yearlvl):
#             super().__init__(name,age,address)
#             self.yearlvl = yearlvl
      
#       def studentinfo(self):
#             print("Name : {} \n Age : {} \n Address : {} \n Yearlvl : {}\n".format(self.name,self.age,self.address,self.yearlvl))

#       def addstudent(self):
#             super().saveinformation("student")

# class Teacher(Person):
#       def __init__(self,name,age,address,yearlvl):
#             super().__init__(name,age,address)
#             self.yearlvl = yearlvl
      
#       def teacherinfo(self):
#             print("Name : {} \n Age : {} \n Address : {} \n Yearlvl : {}\n".format(self.name,self.age,self.address,self.yearlvl))

#       def addteacher(self):
#             super().saveinformation("teacher")
      

# class View:
#       @staticmethod
#       def showinfo():
#             print("Name | Age | Address | Type")
#             for info in info_list:
#                   print("{} | {} | {} | {} \n".format(info["name"],info["age"],info["address"],info["type"]))
#             return False

# student1 = Student("Jan",25,"Cebu",3)
# student1.addstudent()
# student2 = Student("Hiro",25,"Cebu",3)
# student2.addstudent()
# #print(View().showinfo())

# teacher1 = Teacher("Michel",44,"Cebu",5)
# teacher1.addteacher()
# #print(View().showinfo())

# os.system("clear")
# x = input("Enter a number : ")
# os.system("clear")
# y = input("Enter a number")



# import os
# import subprocess as np

# info_list = []
# class Person:
#       def __init__(self,name,age,address):
#             self.name = name
#             self.age = age
#             self.address = address
#             self.info_list = []
#       def information(self):
#             print("Name : {} \n Age : {} \n Address : {} \n".format(self.name,self.age,self.address))
#       def saveinformation(self,wtype):
#             information_dict = {"name":self.name , "age":self.age , "address":self.address , "type":wtype}
#             info_list.append(information_dict)
#       #def getinformation(information):
#       #      return self.info_list

# class Student(Person):
#       def __init__(self,name,age,address,yearlvl):
#             super().__init__(name,age,address)
#             self.yearlvl = yearlvl
      
#       def studentinfo(self):
#             print("Name : {} \n Age : {} \n Address : {} \n Yearlvl : {}\n".format(self.name,self.age,self.address,self.yearlvl))

#       def addstudent(self):
#             super().saveinformation("student")

# class Teacher(Person):
#       def __init__(self,name,age,address,yearlvl):
#             super().__init__(name,age,address)
#             self.yearlvl = yearlvl
      
#       def teacherinfo(self):
#             print("Name : {} \n Age : {} \n Address : {} \n Yearlvl : {}\n".format(self.name,self.age,self.address,self.yearlvl))

#       def addteacher(self):
#             super().saveinformation("teacher")
      

# class View:
#       @staticmethod
#       def showinfo():
#             print("Name | Age | Address | Type")
#             for info in info_list:
#                   print("{} | {} | {} | {} \n".format(info["name"],info["age"],info["address"],info["type"]))
#             return False

# # student1 = Student("Jan",25,"Cebu",3)
# # student1.addstudent()
# # student2 = Student("Hiro",25,"Cebu",3)
# # student2.addstudent()
# # #print(View().showinfo())

# # teacher1 = Teacher("Michel",44,"Cebu",5)
# # teacher1.addteacher()
# # #print(View().showinfo())

# while True:
#       print("Welcome to Enrollment System")
#       print("[1] Student")
#       print("[2] Teacher")
#       print("[3] ShowInformations")
#       print("[4] Exit")
#       number = int(input("Your Choice :"))
      
#       if number == 1:
#             os.system("clear")
#             name = input("Name :")
#             age = input("Age :")
#             address = input("Address :")
#             yearlvl = input("Yearlvl :")
#             student = Student(name,age,address,yearlvl)
#             student.addstudent
#             continue
#       elif number == 2:
#             os.system("clear")
#             name = input("Name :")
#             age = input("Age :")
#             address = input("Address :")
#             yearlvl = input("Yearlvl :")
#             teacher = Teacher(name,age,address,yearlvl)
#             teacher.addteacher
#             continue
#       elif number == 3:
#             os.system("clear")
#             View().showinfo()
#       elif number == 4:
#             break


import os

author_list = []
class Author:
      def __init__(self,name,age,address):
            self.name = name
            self.age = age
            self.address = address
            self.author_list = []
      
      def author_info(self):
            print("Name : {} \n  Age : {} \n  Address : {} \n".format(self.name,self.age,self.address))
      
      def author_save(self):
            author_dict = {"name":self.name,"age":self.age,"address":self.address}
            author_list.append(author_dict)

book_list = []
class Book:
      def __init__(self,title,genre,author):
            self.title = title
            self.genre = genre
            self.author = author
            self.book_list = []
      
      def book_info(self):
            print("Title : {} \n  Genre : {} \n  Author : {} \n".format(self.title,self.genre,self.author))
      
      def book_save(self):
            book_dict = {"title":self.title,"genre":self.genre,"author":self.author}
            book_list.append(book_dict)

class Viewauthor:
      @staticmethod
      def authorinfo():
            print("Name | Age | Address ")
            for info in author_list:
                  print("{} | {} | {} \n".format(info["name"],info["age"],info["address"]))
                  return False

class Viewbook:
      @staticmethod
      def bookinfo():      
            print("Title | Genre | Author ")
            for info in book_list:
                  print("{} | {} | {} \n".format(info["title"],info["genre"],info["author"]))
                  return False


while True:

      print("Welcome to Enrollment System")
      print("[1] Author")
      print("[2] Book")
      print("[3] Author List")
      print("[4] Book List")
      print("[5] Exit")
      choice = int(input("Your Choice :"))

      if choice == 1:
            os.system("clear")
            name = input("Enter name :")
            age = input("Enter age :")
            address = input("Enter address :")
            author = Author(name,age,address)
            author.author_save()
      
      elif choice  == 2:
            if len(author_list)>0:
                  os.system("clear")
                  title = input("Enter title :")
                  genre = input("Enter genre :")
                  author_number = int(input("Enter author_number :"))
                  book = Book(title,genre,author_list[author_number])
            else:
                  continue

      elif choice == 3:
            os.system("clear")
            Viewauthor().authorinfo()
      
      elif choice == 4:
            os.system("clear")
            Viewbook().bookinfo()
      else:
            break
