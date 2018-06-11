import random
import time
from Classes.config_util import  config_meta
import logging

logging.basicConfig(filename=config_meta.LOG_FILENAME, level=logging.DEBUG)
my_logger = logging.getLogger(__name__)

class account_info:
    

  branchList =['R.R.Nagr','whitefiled','Marathalli']

  def __init__(self, account_no, current_balance, bank_name, bank_branch, account_type, account_id=None):
        self.accountid=random.randint(1,100)
        #self.database_connection= database_connection
        my_logger.info('---initializing Account info for user---')
        #self.dbCursor = dbCursor
        self.accountno='IND-'+str(int(time.time()))
        self.accountBank=random.choice(account_info.branchList)
        self.currentBalance=1.00*random.randint(2000,8000)
        self.Bank_name="IndiGo Bank"
        self.accountType='Savings'
       
  def display_account(self):
    print ("account_no : ", self.account_no)
    
  def __str__(self):
    return "account_id :-{}  account_no:-{}".format(self.account_id,self.account_no) 
     
