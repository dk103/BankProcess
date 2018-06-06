#!C:\Users\M1030512\AppData\Local\Programs\Python\Python36\python.exe


import cgi, cgitb
import logging

from Classes import config_meta
from Classes import user_Details_services





import models;

logging.basicConfig(filename=config_meta.LOG_FILENAME, level=logging.DEBUG)
my_logger = logging.getLogger(__name__)
# Create the form object
frmEmp = cgi.FieldStorage()

# Get the values
firstname = frmEmp.getvalue("firstname")
lastname = frmEmp.getvalue("lastname")
username = frmEmp.getvalue("username")
password = frmEmp.getvalue("password")
gender = frmEmp.getvalue("gender")
dob = frmEmp.getvalue("dob")
address = frmEmp.getvalue("address")
pincode = frmEmp.getvalue("pincode")

my_logger = logging.getLogger(__name__)
my_logger.debug('---user value request success')
#user = models.user(username, firstname, lastname, dob, address, password, pincode, gender)
user = models.user("abc@zy.com", "sam", "trik", "11-july-1992", "12345", "M103456", "1111123", "M")
user_Details_services = user_Details_services()
res = user_Details_services.user_registration(user)

if(res == True):
  my_logger.debug('---user successfuly  inserted request success')
  print ("Content-Type: text/html\r\n")
  print ("<h3>Users Registered Successfully....<a href='./index.html'><span style='color:yellow'>plz Login </span></a></h3><br>")

else:
  my_logger.debug('---Registration of user failed')
  print ("Content-Type: text/html\r\n")
  print ("<h3><span style='color:red'>Please Register again ....</span></h3><br>")

