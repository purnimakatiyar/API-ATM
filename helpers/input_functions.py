from controllers.user import User
from utils.validators import Validation
from configurations import prompts
import maskpass


class InputFunctions:
    
    
    def customer_add_input(self):
        unique_id = input(prompts.UNIQUE_ID)
        while Validation.validate_id(unique_id) == False:
            unique_id = input(prompts.VALID_UNIQUE_ID)
             
        security_code = maskpass.advpass(prompt = prompts.SECURITY_CODE, mask = "*")
       
        account_number = input(prompts.ACCOUNT_NUMBER)
        while Validation.validate_account_number(account_number) == False:
            account_number = input(prompts.VALID_ACCOUNT_NUMBER)
        
        name = input(prompts.NAME)    
        while Validation.validate_account_number(account_number) == False:
            name = input(prompts.VALID_NAME)
            
        balance = input(prompts.BALANCE)

        account_type = input(prompts.ACCOUNT_TYPE)
        while Validation.validate_account_type(account_number) == True:
            account_type = input(prompts.VALID_ACCOUNT_TYPE)

        return (unique_id, security_code, account_number, name, balance, account_type)
    
    
    def delete_customer_input(self):
        unique_id = input(prompts.DELETE_CUSTOMER)
        return unique_id
       
        
    def unique_id_input(self):
        return input(prompts.AUTH_UNIQUE_ID) 
    
    
    def security_code_input(self):
        return maskpass.advpass(prompt = prompts.AUTH_SECURITY_CODE, mask = "*")
        
        
    def valid_unique_id_input(self):
        unique_id = input(prompts.VALID_UNIQUE_ID)
        return unique_id 
        
        
    def deposit_money_input(self):
        amount = input(prompts.DEPOSIT_AMOUNT)
        return amount
        
        
    def Withdraw_money_input(self):
        amount = input(prompts.WITHDRAW_AMOUNT)
        return amount
  
  
    def change_security_code_input(self):
        new_security_code = maskpass.advpass(prompt = prompts.NEW_SECURITY_CODE, mask = "*")
        return new_security_code