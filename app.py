from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from resources.authenticate import blp as AuthBlueprint
from resources.account import blp as AccountBlueprint
from resources.user import blp as UserBlueprint

from controllers.authenticate import Authenticate


def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "ATM System API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['DEBUG'] = True


    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "25339446708963499269000046428341264752"
    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_role_to_claims(identity):
        result = Authenticate(unique_id = identity).check_role()
        return {"role": result}
    
        
    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(AccountBlueprint)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)



# from views.menu import Menu
# from models.db import Database

# def main():
#     Menu().login()
#     Database().close()
    
# if __name__ == '__main__':
#     main()