from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import AuthSchema
from controllers.authenticate import Authenticate
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import get_jwt
from blocklist import BLOCKLIST
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token


blp = Blueprint("Auth", "auth", description="Authenticate operations")


@blp.route('/login')
class AuthenticateView(MethodView):
    
    @blp.arguments(AuthSchema)
    def post(self, auth_data):
        auth = Authenticate(unique_id = auth_data["Unique_id"])
        user_password = auth.check_credentials()
        if user_password and pbkdf2_sha256.verify(auth_data["Security_code"], user_password):
            access_token = create_access_token(identity=auth_data["Unique_id"], fresh=True)
            refresh_token = create_refresh_token(identity=auth_data["Unique_id"])
            return {"access_token": access_token, "refresh_token": refresh_token}
        abort(401, message="Invalid credentials")
        
        
@blp.route("/refresh")
class RefreshToken(MethodView):

    @jwt_required(refresh=True)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}
    
@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 204

# pbkdf2_sha256.hash(auth_data["Security_code"])