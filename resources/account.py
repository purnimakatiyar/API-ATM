from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import get_jwt_identity, jwt_required
from schemas import BalanceSchema
from controllers.account import Account
from utils.rbac import role_access

blp = Blueprint("Account", "account", description="Account operations")

@blp.route('/balance')
class AccountBalance(MethodView):
    
    @jwt_required()
    @role_access(['Customer'])
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        user_id = get_jwt_identity()
        result = Account(unique_id = user_id).view_balance()
        if result == -1:
            abort(404, message = "User does not exists")
        else:
            return {
            "balance": result}, 200
    
    

@blp.route('/deposit')
class AccountDeposit(MethodView):
    
    @jwt_required()
    @role_access(['Customer'])
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(BalanceSchema)
    def put(self, balance_data):
        user_id = get_jwt_identity()
        result = Account(unique_id = user_id).deposit_money(balance_data["amount"])
        if result == -1:
            abort(401, message = "User does not exists")
        else:
            return {
            "message": "Deposit successfully"}, 200
     
     
        
@blp.route('/withdraw')
class AccountWithdraw(MethodView):
    
    @jwt_required()
    @role_access(['Customer'])
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(BalanceSchema)
    def put(self, balance_data):
        user_id = get_jwt_identity()
        result = Account(unique_id = user_id).withdraw_money(balance_data["amount"])
        if result == -1:
            abort(404, message = "User does not exists or insufficient balance")
        else:
            return {
            "message": "Withdrawn successfully"}, 200
       
       
@blp.route('/transactions')
class TransactionView(MethodView):
    
    @jwt_required()
    @role_access(['Customer'])
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        user_id = get_jwt_identity()
        result = Account(unique_id = user_id).view_recent_transactions()
        if result == -1:
            abort(404, message = "No records found.")
        else:
            return {
                "result": result}, 200