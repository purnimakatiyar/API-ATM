from marshmallow import Schema, fields

class AuthSchema(Schema):
    Unique_id = fields.Str(required = True)
    Security_code = fields.Str(required = True)
    
class UserSchema(Schema):
    Unique_id = fields.Str(required = True)
    Security_code = fields.Str(required = True)
    # Email = fields.Str(required=True)
    Account_Number = fields.Str(required = True)
    Name = fields.Str(required = True)
    Balance = fields.Str(required = True)
    Account_type = fields.Str(required = True)
    
class RemoveSchema(Schema):
    Unique_id = fields.Str(required = True)
    
class BalanceSchema(Schema):
    amount = fields.Str(required = True)
    
class UserUpdateSchema(Schema):
    Security_code = fields.Str(required = True)
    