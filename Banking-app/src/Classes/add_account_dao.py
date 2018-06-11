import logging
import pymysql
from Classes.config_util import  config_meta
import time
import random
from models import account_info_model
from Classes.connectionDetails import connection_Details


logging.basicConfig(filename=config_meta.LOG_FILENAME, level=logging.DEBUG)
my_logger = logging.getLogger(__name__)

class account_dao(object):
    
    
    
    def __init__(self,database_connection,dbCursor):
        my_logger.info('---initializing Account info for user---')
        self.database_connection= database_connection
        self.dbCursor = dbCursor
       
    def connectToDb(self):
        try:
           self.database_connection = pymysql.connect(host = '127.0.0.1',port = 3306,user = connection_Details.user,passwd = connection_Details.user,db = connection_Details.databaseName)
           #pymysql.connect(connection_Details.serverName, connection_Details.user, connection_Details.dbPassword, connection_Details.databaseName)
           my_logger.info("Connection Established")
           self.dbCursor = self.database_connection.cursor()
        except Exception as e:
          pass
          my_logger.info("Connection Declined")
          my_logger.error ("Connection Error ->", exc_info=True)        
        
        
        
    def  register_Account(self,account_model):
      my_logger.info('---adding Account info for user---')
      try: 
           sql = "INSERT INTO account_info(account_id,account_no,current_balance,bank_name,bank_branch,account_type) \
                  VALUES (%d,'%s', %.2f, '%s', '%s', '%s')" % \
                  (account_model.accountid,account_model.accountno,account_model.currentBalance,account_model.Bank_name,account_model.accountBank,account_model.accountType)
           my_logger.info(sql)
           self.dbCursor.execute(sql)
           self.database_connection.commit()
           my_logger.info(self)
           return account_model.accountid 
      except Exception as e:
           self.database_connection.rollback()
           my_logger.exception("Unable to insert account records:-")          
#       finally:
#            if(self.database_connection != None):
#               self.database_connection.close()
#            if(self.dbCursor != None):
#               self.dbCursor = None
                  
      return -1
  
    def get_Account_details(self,recepient_accountNo,userAccountId):
     msg= None  
     sql =None
     my_logger.info('---fecting account  info---')
     try:
        if(recepient_accountNo!=None):
            sql = "SELECT account_no,current_balance,bank_name,bank_branch,account_type from  account_info where account_no='%s'" % (recepient_accountNo)
        else: 
            sql = "SELECT account_no,current_balance,bank_name,bank_branch,account_type from  account_info where account_id=%d" % (int(userAccountId))
              
        my_logger.info(sql)
        self.dbCursor.execute(sql)
        account_details = self.dbCursor.fetchone()
        if (account_details != None):
            account_no = account_details[0]
            current_balance=(account_details[1])
            bank_name=account_details[2]
            bank_branch=account_details[3]
            account_type=account_details[4]
            msg=account_no+","+bank_name+","+bank_branch+","+account_type+","+str(current_balance)
            return msg

         
     except Exception as e:
         print ("exception while fecting account->", e)
         msg="500"          
#      finally:
#         if(user_details_dao.database_connection != None):
#             user_details_dao.database_connection.close()    
#         if(user_details_dao.dbCursor != None):
#             dbCursor = None                
     return msg
 
    def get_Account_Balance(self,userAccountId):
     msg= None  
     my_logger.info('---fecting account  balance---')
     try: 
        sql = "SELECT current_balance  from  account_info where account_id=%d" % (int(userAccountId))
        my_logger.info(sql)
        self.dbCursor.execute(sql)
        account_details = self.dbCursor.fetchone()
        if (account_details != None):
            current_balance=str(account_details[0])
            msg=current_balance
            return msg

         
     except Exception as e:
         print ("exception while fecting account->", e)
         msg="500"          
#      finally:
#         if(user_details_dao.database_connection != None):
#             user_details_dao.database_connection.close()    
#         if(user_details_dao.dbCursor != None):
#             dbCursor = None                
     return msg     
 
 
    def getAccountNo(self,recipient,dispatcher,type):
         accountList=[]
         sql = None
         results =None
         my_logger.info('---fecthing account no on basis of account---')
         try: 
            if(type=="deposit" or type =="None" or type=="transfer"):
                sql = "SELECT  account_no   FROM account_info  where account_id=%d" % (int(dispatcher))
                self.dbCursor.execute(sql)
                results =  self.dbCursor.fetchall()
                for row in results:
                  if (row != None):
                     dispatcher_account_no = row[0]
                     accountList.append(dispatcher_account_no)
            if(type=="transfer"):
                sql = "SELECT  account_no   FROM account_info  where account_id=%d" % (int(recipient))
                self.dbCursor.execute(sql)
                results =  self.dbCursor.fetchall()
                for row in results:
                  if (row != None):
                     recipient_account_no = row[0]
                     accountList.append(recipient_account_no) 
            return accountList
         except Exception as e:
             print ("exception while checking username ->", e)          
         finally:
           if(self.database_connection != None):
               self.database_connection.close()    
           if(self.dbCursor != None):
               self.dbCursor = None                
         return accountList
             
    