from .database import Database

class Schedule:
      def __init__(self,schedule_name,schedule_code):
            self.schedule_name = schedule_name
            self.schedule_code = schedule_code
            self.__csvfile = 'data/schedule.csv'
      
      def information(self):
            print("Name : {} \n Code : {} \n ".format(self.schedule_name,self.schedule_code))

      def saveinformation(self):
            last_id = Database([],self.__csvfile).id_ai()
            student = [last_id+1,self.schedule_name,self.schedule_code]
            Database([student],self.__csvfile).savedata()
