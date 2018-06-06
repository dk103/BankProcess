import time
class transactions:

   def __init__(self, transaction_type, amount, recipient_account_number, recipient_account_bank, user_id, transaction_id=None):
     self.transaction_id = transaction_id
     self.transaction_type = transaction_type
     self.amount = amount
     self.recipient_account_number = recipient_account_number
     self.recipient_account_bank = recipient_account_bank
     self.transaction_no= str(int(time.time()))
     self.user_id=user_id
     
   def display(self):
     print("transaction_id:-", self.transaction_id)

   def __str__(self):
      return "transaction_id :-{}  user_id:-{}  transaction_no:-{}".format(self.transaction_id,self.user_id,self.transaction_no) 