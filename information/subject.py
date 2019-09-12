from .database import Database

class Subject:
      def __init__(self,subject_name,subject_code):
            self.subject_name = subject_name
            self.subject_code = subject_code
            self.__csvfile = 'data/subject.csv'
      
      def information(self):
            print("Name : {} \n Code : {} \n ".format(self.subject_name,self.subject_code))

      def saveinformation(self):
            last_id = Database([],self.__csvfile).id_ai()
            student = [last_id+1,self.subject_name,self.subject_code]
            Database([student],self.__csvfile).savedata()
