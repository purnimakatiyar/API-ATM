import re

class Validation:

    @staticmethod
    def validate_id(unique_id):
        return bool(re.match(r"^\d+$",unique_id))
    
    @staticmethod
    def validate_account_number(account_number):
        return bool(re.match(r"^\d{10,}$", account_number))
    
    @staticmethod
    def validate_account_number(account_number):
        if not account_number:
            return False
        if not account_number.isdigit():
            return False
        if 8 <= len(account_number) <= 12:
            return True
        return False
    
    @staticmethod
    def validate_name(name):
        if isinstance(name, str):
            return True
        return False
    
    @staticmethod
    def validate_account_type(account_type):
        valid_types = ["savings", "current"]
        if account_type.lower() in valid_types:
            return True
        return False