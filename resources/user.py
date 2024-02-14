from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema, RemoveSchema, UserUpdateSchema
from controllers.user import User
from flask_jwt_extended import jwt_required
from passlib.hash import pbkdf2_sha256
from utils.rbac import role_access


blp = Blueprint("User", "user", description="User operations")


# def send_simple_message(_, to, subject, body):
#     domain = os.getenv("MAILGUN_DOMAIN")
#     return requests.post(
# 		f"https://api.mailgun.net/v3/{domain}/messages",
# 		auth=("api", os.getenv("MAILGUN_API_KEY")),
# 		data={"from": "Excited User <mailgun@{domain}}>",
# 			"to": [to],
# 			"subject": subject,
# 			"text": body})


@blp.route('/user')
class UserView(MethodView):
    
    
    @jwt_required()
    @role_access(['Admin'])
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(UserSchema)
    def post(self, user_data):
        
        user = User(
                unique_id = user_data["Unique_id"],
                security_code = pbkdf2_sha256.hash(user_data["Security_code"]),
                account_number = user_data["Account_Number"],
                name = user_data["Name"],
                balance = user_data["Balance"],
                account_type = user_data["Account_type"]
                )
        
        result = user.add_customer()
        if result == -1:
            abort(409, message = "User already exists")
        else:
            
            # send_simple_message(
            #     email = user_data["Email"],
            #     to=user.email,
            #     subject="Successfully signed up",
            #     body=f"Hi {user.username}! You have successfully signed up to the ATM System API"
                
            # )
            return {
            "message": "User added successfully"}, 201
        
        
        
@blp.route('/user/<user_id>')
class DeleteUserView(MethodView):
    
    @jwt_required()
    @role_access(['Admin'])
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def delete(self, user_id):
      
        user = User()
        result = user.remove_customer(user_id)
        if result == -1:
            return {
            "message": "User removed successfully"}, 200
        else:
            abort(404, message = "User does not exists")
       
        
        
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(UserUpdateSchema)
    def put(self, user_data):
        
        user = User()
        user.change_security_code(user_data["Security_code"])
        return {
            "message": "Security code changed successfully"}, 201
        
