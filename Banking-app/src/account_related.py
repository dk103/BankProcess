#!C:\Users\M1030512\AppData\Local\Programs\Python\Python36\python.exe

import cgi, cgitb

import sys
import logging
import hashlib
import time
from Classes import user_Details_services
from Classes import config_meta
from Classes import payee_services
from models import beneficiaries_details
import cgi, os 
from http import cookies



logging.basicConfig(filename=config_meta.LOG_FILENAME, level=logging.DEBUG)

my_logger = logging.getLogger('account module')
my_logger.info('---processing account modules---')
cookie = cookies.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
#cookie_string ="accountId=40"
 
if(cookie_string!=None):
    cookie.load(cookie_string)
    config_meta.Session_userAccountId = cookie['accountId'].value

    
    



frmEmp = cgi.FieldStorage()


# querytype = frmEmp.getvalue("optype")
# uid=frmEmp.getvalue("sid")

querytype="ACCOUNT_INFO"
uid=780

my_logger.info('querytype:-'+querytype+ 'uid:-'+str(uid))

logging.info('account holder id:-'+ str(config_meta.Session_userAccountId))

user_Details_services = user_Details_services()

config_meta.Session_userAccountId=40
res = user_Details_services.showAccountDetails(config_meta.Session_userAccountId)

#res = user_Details_services.showAccountDetails(40)

if(res != "500" and res!=None): 
  list = res.split(",")
  my_logger.debug('---Fetched account details successfully')
  print ("Content-Type: text/html\r\n")
  print ("<div class='card'><div class='card-header bg-info d-flex justify-content-center'><Strong>ACCOUNT DETAILED INFO:</Strong></div><div class='card bg-light '><div class='card-body'><span style='color: blue' id='err'></span><br><div class='col-xs-12'><h2>Customer Account Info:</h2><table id='accTable'  ><tr><th>Account No:</th><td>{}</td></tr>     <tr> <th>Bank Name:</th><td>{}</td></tr>  <tr>  <th>Bank Branch:</th><td>{}</td></tr><tr>   <th>Account Type:</th><td>{}</td></tr><tr><th>Current Balance</th><td>{}</td></tr></table></div><div class='col-xs-12'><input type='hidden' id='CurrentBalance' value={}></div></div></div>  </div>"
         .format(list[0],list[1],list[2],list[3],list[4],str(list[4])))
else:
     my_logger.debug('---Fetched account details Failed')
     print ("Content-Type: text/html\r\n")
#    

     print("<div class='card'><div class='card-header bg-info d-flex justify-content-center'><Strong>ACCOUNT DETAILED INFO:</Strong></div><div class='card bg-light'><div class='card-body'><h3><span style='color:red' class='glyphicon glyphicon-thumbs-down'>&nbsp;Sorry.......</span></h3><br><div class='col-xs-12' ><img class='img-fluid  w-100 img-responsive' src='../images/error404.png' ></div></div></div></div>")
     