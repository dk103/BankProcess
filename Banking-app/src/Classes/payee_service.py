

from Classes.payee_dao import payee_dao_access
import logging
from Classes.config_util import config_meta
from models import beneficiaries_details

logging.basicConfig(filename=config_meta.LOG_FILENAME, level=logging.DEBUG)
my_logger = logging.getLogger("payee_service")


class payee_services:
      def __init__(self):
         self.payee_dao_access = payee_dao_access()
        
      def add_payee(self,payee):
         my_logger.info('--- inside add_payee service---')
         self.payee_dao_access.connectToDb()
         res = self.payee_dao_access.beneficiariesAccountInclusion(payee)
         if (res != None):
                return res
         return None
     
      def remove_payee(self,payee):
         my_logger.info('--- inside remove_payee service---')
         self.payee_dao_access.connectToDb()
         res = self.payee_dao_access.beneficiariesAccountRemoval(payee)
         return res
     

      def fetchPayeeList(self,user_id):
          my_logger.info('--- fecth payee list service---') 
          self.payee_dao_access.connectToDb()
          res = self.payee_dao_access.getPayeeList(user_id)
          return res