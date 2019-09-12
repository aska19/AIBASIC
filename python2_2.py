# import  math
# import statistics

# print(2**3)
# print(math.pow(2,3))

# my_list = [2,45,67,23,45]

# mean = statistics.mean(my_list)
# print(mean)  #mean = average

# mediam = statistics.mediam(my_list)
# print(mediam)

# mode = statistics.mode(my_list)
# print(mode)


# print(dir(math))  #dir mathのメゾットが出てくる
# print(dir(statistics))

# print(dir(Information))
# print(Information)


# from information.information import Information,info_list
# from information.student import Student
# from information.teacher import Teacher

# import os

# class View:
#       @staticmethod
#       def showinfo():
#             print("Name | Age | Address | Type")
#             for info in info_list:
#                   print("{} | {} | {} | {} \n".format(info["name"],info["age"],info["address"],info["type"]))
#             return False

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


# from information.information import Information,info_list
# from information.student import Student
# from information.teacher import Teacher
# import os
# import csv

# with open('information.csv','r') as rf:
#       reader = csv.reader(rf)
#       header = next(reader)

#       for row in reader:
#             print(row)

# with open('information.csv','w') as wf:   #w = write
#       writer = csv.writer(wf)
#       writer.writerow(['name','age','addresss','type'])
#       # writer.writerow(['Jan','25','Cebu','Teacher'])
#       writer.writerows([['Jan','25','Cebu','Teacher'],['John','30','Cebu','Teacher']])

# from information.information import Information,info_list
# from information.student import Student
# from information.teacher import Teacher

# import os
# import csv

# student_list = []
# with open('information.csv','r') as rf:
#       reader = csv.reader(rf)
#       header = next(reader)
#       for row in reader:
#             student_list.append(row)
# while True:
#       name = input('Enter your name :')
#       age = input('Enter your age :')
#       address = input('Enter your address :')
#       types = input('Enter your type :')
#       choice = input('You want to add more? Y/N :')
#       student_list.append([name,age,address,types])
      
#       if choice == 'Y':
#             continue
#       elif choice == 'N':
#             with open('information.csv','w',newline='') as wf:
#                   writer = csv.writer(wf)
#                   writer.writerow(['name','age','addresss','type'])
#                   writer.writerows(student_list)
#             break


# from information.information import Information,info_list
# from information.student import Student
# from information.teacher import Teacher
# from information.database import Database

# import os
# import csv

# while True:
#       name = input('Enter your name :')
#       age = input('Enter your age :')
#       address = input('Enter your address :')
#       types = input('Enter your type :')
#       choice = input('You want to add more? Y/N :')
#       Database([[name,age,address,types]]).savedata(['name','age','address','types'])
      
#       if choice == 'Y':
#             continue
#       elif choice == 'N':
#             break

from information.information import Information
from information.student import Student
from information.teacher import Teacher
from information.database import Database
from information.subject import Subject
from information.course import Course
from information.schedule import Schedule

import os
import csv

while True:
      print("Welcome to Enrollment System")
      print("[1] Student")
      print("[2] Teacher")
      print("[4] Course")
      print("[5] Subject")
      print("[6] Schedule")
      print("[7] ShowInformations")
      print("[0] Exit")
      choice = int(input("Your Choice :"))
      
      if choice == 1:
            os.system("clear")
            name = input("Name :")
            age = input("Age :")
            address = input("Address :")
            yearlvl = input("Yearlvl :")
            student = Student(name,age,address,yearlvl)
            student.addstudent()
            continue
      elif choice == 4:
            os.system('clear')
            course_name = input('Course Name :')
            course_code = input('Course Code :')
            course = Course(course_name,course_code)
            course.saveinformation()
            continue

      elif choice == 5:
            os.system('clear')
            subject_name = input('Subject Name :')
            subject_code = input('Subject Code :')
            subject = Subject(subject_name,subject_code)
            subject.saveinformation()
            continue
      
      elif choice == 6:
            os.system('clear')
            schedule_name = input('Schedule Name :')
            schedule_code = input('Schedule Code :')
            schedule = Schedule(schedule_name,schedule_code)
            schedule.saveinformation()
            continue
      
      elif choice == 3:
            continue
      elif choice == 4:
            break