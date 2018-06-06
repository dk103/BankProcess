import random
class beneficiaries_details:

  def __init__(self, beneficiaries_account_number, beneficiaries_account_holder, beneficiaries_bank, user_id, beneficiaries_id=None):
    
     self.beneficiaries_id = random.randint(120,180)
     self.beneficiaries_account_number = beneficiaries_account_number
     self.beneficiaries_account_type = "Savings A/c"
     self.beneficiaries_bank = beneficiaries_bank
     self.beneficiaries_account_holder = beneficiaries_account_holder
     self.user_id = user_id
  def display(self):

    print ("beneficiaries_account_holder:", self.beneficiaries_account_holder)

  def __str__(self):
       return "beneficiaries_id :-{}  beneficiaries_account_number:-{}".format(self.beneficiaries_id,self.beneficiaries_account_number)