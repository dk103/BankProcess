#!C:\Users\M1030512\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb
import sys
import logging

from Classes import config_meta
from Classes import user_Details_services



logging.basicConfig(filename=config_meta.LOG_FILENAME, level=logging.DEBUG)

# Create the form object
frmEmp = cgi.FieldStorage()

# Get the values
userName = frmEmp.getvalue("userid")
password = frmEmp.getvalue("pswrd")


my_logger = logging.getLogger('user_login')
my_logger.info('---processing  user login')
#user = models.user("abc@zy.com", "sam", "trik", "11-july-1992", "12345", "M103456", "1111123", "M")
user_Details_services = user_Details_services()
res = user_Details_services.login_details_Validation(userName,password)

if(res != None):
  my_logger.debug('---user logged id in successfully')
  print ("Content-Type: text/html\r\n")
  print ("Location:'Dashboard.html'\n\n")
  
  print ("<h3><span style='color:green' class='glyphicon glyphicon-thumbs-up'></span> Registered Successfully..<a href='./index.html'><span style='color:yellow'> plz Login </span></a></h3><br>")

else:
  my_logger.debug('---Logged in Failed')
  print ("Content-Type: text/html\r\n")
  print ("<h3><span style='color:red' class='glyphicon glyphicon-thumbs-down'> Retry </span></h3><br>\
          <p style='color:red'>Username or password not matching<p>")

