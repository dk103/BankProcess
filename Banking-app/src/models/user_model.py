import random
class user:

   def __init__(self, user_name, first_name, last_name, Date_of_Birth, address, password, pin_code, gender, user_id=None):  
         self.userid = random.randint(300,900)
         self.username = user_name  
         self.firstname = first_name
         self.lastname = last_name
         self.dob = Date_of_Birth
         self.address = address
         self.password = password
         self.pincode = pin_code
         self.gender = gender
         
   def displayUSer(self):
  
      print ("user_name : ", self.username, ", name: ", self.firstname)
      
   def __str__(self):
       return "user_name :-{}  user_id:-{}".format(self.username,self.userid)
      
            
