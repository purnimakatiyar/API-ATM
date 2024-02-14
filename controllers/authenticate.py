from models.db import Database
from configurations import queries


class Authenticate:

    def __init__(self, **auth_details):
        self.unique_id = auth_details.get('unique_id')
        self.security_code = auth_details.get('security_code')
        self.db = Database()
       

    def check_credentials(self):
        check_password = self.db.get_item(queries.SEARCH_PASSWORD, (self.unique_id,))
        if check_password is not None:
            return check_password[0]
        else:
            return check_password
    
    
    def check_role(self):
        role = self.db.get_item(queries.CHECK_ROLE, (self.unique_id,))
        return role[2]  
    