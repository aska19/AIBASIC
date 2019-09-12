# info_list = []
# class Information:
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
#       def getinformation(self):
#            return self.info_list


from .database import Database

class Information:
      def __init__(self,name,age,address):
            self.name = name
            self.age = age
            self.address = address
            self.__csvfile = 'information.csv'
      def information(self):
            print("Name : {} \n Age : {} \n Address : {} \n".format(self.name,self.age,self.address))
      def saveinformation(self,wtype):
            student = [self.name,self.age,self.address,wtype]
            Database([student],self.__csvfile).savedata()