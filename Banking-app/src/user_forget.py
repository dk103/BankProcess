#!C:\Users\M1030512\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb
import sys
import logging
import hashlib
import time

from Classes import config_meta
from Classes import user_Details_services



logging.basicConfig(filename=config_meta.LOG_FILENAME, level=logging.DEBUG)

# Create the form object
frmEmp = cgi.FieldStorage()

# Get the values
userName = frmEmp.getvalue("username")
password = frmEmp.getvalue("password")


my_logger = logging.getLogger('user_Password Change')
my_logger.info('---processing  user password change---')
#user = models.user("abc@zy.com", "sam", "trik", "11-july-1992", "12345", "M103456", "1111123", "M")
user_Details_services = user_Details_services()
#res = user_Details_services.password_change_proc('vasumaj13@yahoo.com','M1040123')

res = user_Details_services.password_change_proc(userName,password)
my_logger.info("db response:-"+str(res))
if(res == "Passed"):
  my_logger.info('---user password updated successfully')


  print ("Content-Type: text/html\r\n")
  print ("<h3><span style='color:green' class='glyphicon glyphicon-thumbs-up'></span> Password updated  Successfully..</h3><br>")

  
 
elif(res=="500"):
  my_logger.info('---Password updation  Failed')
  print ("Content-Type: text/html\r\n")
  print ("<h3><span style='color:red' class='glyphicon glyphicon-thumbs-down'> Retry </span></h3><br>\
          <p style='color:red'>Internal problem occured<p>")

else:
  my_logger.info('---Password updation  Failed')
  print ("Content-Type: text/html\r\n")
  print ("<h3><span style='color:red' class='glyphicon glyphicon-thumbs-down'> Retry </span></h3><br>\
          <p style='color:red'>{}<p>".format(res))