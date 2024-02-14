from configurations import menu_prompts
from utils.validators import Validation
from helpers.input_functions import InputFunctions
from controllers.account import Account
from controllers.user import User
from controllers.authenticate import Authenticate
from configurations import prompts
from configurations import menu_prompts

class Menu:
    
    def __init__(self):
        self.input = InputFunctions()
        self.auth = Authenticate()
        self.user = User()


    def admin_menu(self, auth_details):
        
        while True:
            print(menu_prompts.ADMIN_MENU)
                
            choice = int(input())
                
            if choice == 1:
                customer_details = self.input.customer_add_input()
                user = User(unique_id = customer_details[0], security_code = customer_details[1], 
                                account_number = customer_details[2], name = customer_details[3],
                                balance = customer_details[4], account_type = customer_details[5])
                user.add_customer()
                
            elif choice == 2:
                unique_id = self.input.delete_customer_input()
                self.user.remove_customer(unique_id)
                
            elif choice == 3:
                user = User(unique_id = auth_details[0], security_code = auth_details[1], 
                         account_number = None, name = None, balance = None, account_type = None)
                new_security_code = self.input.change_security_code_input()
                user.change_security_code(new_security_code)
                
            elif choice == 4:
                exit()
            
            else:
                print(prompts.WRONG_INPUT)
       
            
    def customer_menu(self, auth_details):
        
        while True:
            print(menu_prompts.CUSTOMER_MENU)
            acc = Account(unique_id = auth_details[0])
            user = User(unique_id = auth_details[0])
            choice = int(input())
            
            if choice == 1:
                acc.view_balance()
                
            elif choice == 2:
                amount = self.input.deposit_money_input()
                acc.deposit_money(amount)
        
            elif choice == 3:
                amount = self.input.Withdraw_money_input()
                acc.withdraw_money(amount)
                    
            elif choice == 4:
                acc.view_recent_transactions()
                    
            elif choice == 5:
                new_security_code = self.input.change_security_code_input()
                user.change_security_code(new_security_code)
                
            elif choice == 6:
                exit()
                
            else:
                print(prompts.WRONG_INPUT)
                
                
    def login(self):
        print(menu_prompts.WELCOME)
        unique_id = self.input.unique_id_input()
        while Validation.validate_id(unique_id) == False:
            unique_id = self.input.valid_unique_id_input()
            
        security_code = self.input.security_code_input()
        auth_details = (unique_id, security_code)
        auth = Authenticate(unique_id = unique_id, security_code = security_code) 
         
        if auth.check_credentials():
            _ = User(unique_id = unique_id, security_code = security_code)
            while True:
                role = auth.check_role()
                if role == 'Admin':
                    self.admin_menu(auth_details)
                else:
                    self.customer_menu(auth_details)            
        else:
            print(prompts.WRONG_CREDENTIALS)