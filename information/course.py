from .database import Database

class Course:
      def __init__(self,course_name,course_code):
            self.course_name = course_name
            self.course_code = course_code
            self.__csvfile = 'data/course.csv'
      
      def information(self):
            print("Name : {} \n Code : {} \n ".format(self.course_name,self.course_code))

      def saveinformation(self):
            last_id = Database([],self.__csvfile).id_ai()
            student = [last_id+1,self.course_name,self.course_code]
            Database([student],self.__csvfile).savedata()
