from information import Information

class Teacher(Information):
      def __init__(self,name,age,address,yearlvl):
            super().__init__(name,age,address)
            self.yearlvl = yearlvl
      
      def teacherinfo(self):
            print("Name : {} \n Age : {} \n Address : {} \n Yearlvl : {}\n".format(self.name,self.age,self.address,self.yearlvl))

      def addteacher(self):
            super().saveinformation("teacher")
      